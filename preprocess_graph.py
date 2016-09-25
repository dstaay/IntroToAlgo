# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:21:13 2016

@author: Dennis
"""

#
# Design and implement an algorithm that can preprocess a
# graph and then answer the question "is x connected to y in the
# graph" for any x and y in constant time Theta(1).
#

#
# `process_graph` will be called only once on each graph.  If you want,
# you can store whatever information you need for `is_connected` in
# global variables
#
P = {}
def process_graph(G):
    for x in G:
        P[x] = {}    
    for x in G:
        for u in G[x]:
            if x is not u:
                if u not in P[x]:
                    (P[x])[u] = 1
                if x not in P[u]:
                    (P[u])[x] = 1
                # now look to see if u is perviosly seen elsewhere  
                for y in P:
                    if u in P[y]:
                       #since u found, see if x is already listed as connection 
                       if ((x not in P[y]) and (x is not y)):
                          (P[y])[x] = 1 
                
            

#
# When being graded, `is_connected` will be called
# many times so this routine needs to be quick
#
def is_connected(i, j):
    for k in P[i]:
        if j == k:
            return True
        
    return False

#######
# Testing
#
def test():
    G = {'a':{'b':1},
         'b':{'a':1},
         'c':{'d':1},
         'd':{'c':1},
         'e':{}}
    #process_graph(G)
    #assert is_connected('a', 'b') == True
    #assert is_connected('a', 'c') == False

    G = {'a':{'b':1, 'c':1},
         'b':{'a':1},
         'c':{'d':1, 'a':1},
         'd':{'c':1},
         'e':{}}
    process_graph(G)
    assert is_connected('a', 'b') == True
    assert is_connected('a', 'c') == True
    assert is_connected('a', 'e') == False

test()