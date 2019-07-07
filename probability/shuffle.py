'''
Created on Oct 16, 2017

@author: qiankunhuang
'''
class deck:
    def _init_(self,deck):
        self.deck = deck
class card(object):
    def _init_ (self,type,value):
        self.type=type
        self.value=value
class type:
    spades=1
    hearts=2
    dismonds=3
    clubs=4
import random   
def shuffle_deck(list):
    l = len(list)
    for i in xrange(l-1,-1,-1):
        a = random.randint(0,i)
        list[a],list[i]=list[i],list[a]
    return list
        
        
    
