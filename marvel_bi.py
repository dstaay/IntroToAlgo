# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 14:42:22 2016

@author: Dennis
"""

#
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#
import pickle
import random

with open("smallG.pkl", 'rb') as f:
    marvel = pickle.load(f)
with open("smallChr.pkl", 'rb') as f:
    characters = pickle.load(f)




def create_weighted_graph(bipartiteG, characters):
    G = {}
    j_appear  = 0
    for char in characters:
        G[char] = {}
        for other_char in characters:
            if other_char is not char:
                for comic in bipartiteG[char]:
                    if comic in bipartiteG[other_char]:
                        j_appear += 1
                if j_appear != 0:
                    (G[char])[other_char] = 1.0 * j_appear / (len(bipartiteG[char])  
                                            + len(bipartiteG[other_char]) 
                                            - j_appear)
                    j_appear = 0
  
        

    return G

######
#
# Test

def test():
    bipartiteG = {'charA':{'comicB':1, 'comicC':1},
                  'charB':{'comicB':1, 'comicD':1},
                  'charC':{'comicD':1},
                  'comicB':{'charA':1, 'charB':1},
                  'comicC':{'charA':1},
                  'comicD': {'charC':1, 'charB':1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None

def test2():
    G = create_weighted_graph(marvel, characters)
 

test2()
