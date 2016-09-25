# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:33:12 2016

@author: Dennis
"""

#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
# 
def down_heapify(L, i, node_map):
    # If i is a leaf, heap property holds
    if is_leaf(L, i): 
        return
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if L[i] > L[left_child(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (node_map[L[i][1]],node_map[L[left_child(i)][1]]) = (left_child(i), i)
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        return
    # If i has two children...
    # check heap property
    if min(L[left_child(i)], L[right_child(i)]) >= L[i]: 
        return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if L[left_child(i)] < L[right_child(i)]:
        # Swap into left child
        (node_map[L[i][1]],node_map[L[left_child(i)][1]]) = (left_child(i), i)
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        down_heapify(L, left_child(i), node_map)
        return
    else:
        (node_map[L[i][1]],node_map[L[right_child(i)][1]]) = (right_child(i), i)
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        down_heapify(L, right_child(i), node_map)
        return

def up_heapify(L, i, node_map):
    if i == 0:
        return
    elif L[parent(i)][0] <= L[i][0]:
        return
    else:
        #print("parent ", parent(i)," before ", L[parent(i)])
        
        (node_map[L[parent(i)][1]],node_map[L[i][1]]) = (i, parent(i))
        (L[parent(i)], L[i]) = (L[i],L[parent(i)])
        #print("parent ", parent(i),"after ",L[parent(i)])
        up_heapify(L,parent(i),node_map)
    return

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def remove_min(L):
    L[0] = L.pop()
    down_heapify(L, 0)
    return
    
def heap_remove_min(heap, node_map):
    
    # update node_map 
    node_map[heap[len(heap)-1][1]] = 0
    node_map.pop(heap[0][1])

    
    # pop tail and replace top
    heap[0] = heap.pop(len(heap)-1)
    
    #recheck heap
    down_heapify(heap, 0, node_map)


def dijkstra(G,v):
    #initialize variables
    node_map = {}
    dist_so_far = {}
    final_dist = {}
    
    dist_so_far[0] = (0, v)
    node_map[v] = 0
    

    while len(final_dist) < len(G):
        
        #lock it down (ie. add top of heap to final_dist)
        w = dist_so_far[0][1]
        final_dist[w] = dist_so_far[0][0]
        
        
        for x in G[w]:
            if x not in final_dist:
                if x not in node_map:
                    # node perviously not encountered
                    # calculate value of path
                    dist_calc = final_dist[w] + G[w][x]
                    # push value to bottom of heap
                    dist_so_far[len(dist_so_far)] = (dist_calc, x)
                    # add x node to heap location map
                    node_map[x] = len(dist_so_far)-1
                    # call upheapify
                    up_heapify(dist_so_far, node_map[x], node_map)
                
                # check if new path is shorter than already known
                elif final_dist[w] + G[w][x] < dist_so_far[node_map[x]][0]:
                    dist_so_far[node_map[x]] = (final_dist[w] + G[w][x], x)
                    up_heapify(dist_so_far, node_map[x], node_map)
        #pop off top of heap and continue
        heap_remove_min(dist_so_far, node_map)            
    print(final_dist)
    return final_dist

############
# 
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

test()