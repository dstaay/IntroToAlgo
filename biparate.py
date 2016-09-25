# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 14:07:00 2016

@author: Dennis
"""

# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#

def bipartite(G):
    
    A = []
    #first element of open list is just starting node
    open_list = [G.keys()[0]]
    while len(open_list) > 0:
        current = open_list.pop(0)
        for joining_node in G[current]:
            # check joining_node not in list
            if joining_node in A:
                 return None 
        A.append(current)
        for joining_node in G[current]:
            # now check joining_node's connections, and add to open list if needed
            for possible_A in G[joining_node]:
                if possible_A not in A:
                    if possible_A not in open_list:
                        open_list.append(possible_A)
    return A       
             

    
########
#
# Test

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    #assert (g1 == set([1, 3, 5]) or
    #        g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert g1 == None

test()