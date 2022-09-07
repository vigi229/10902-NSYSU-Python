from functools import reduce, partial
from itertools import zip_longest
from operator import concat, eq, mul
from collections import ChainMap
from copy import copy
from random import randrange as rnd
from numpy import transpose

class Connect4():
    p=ChainMap(dict(zip_longest({'⚪','e','E','h','H','o','O','empty','hollow',
                                 'open','Empty','Hollow','Open','EMPTY','OPEN',
                                 'HOLLOW'},{},fillvalue='⚪')),
               dict(zip_longest({'⚫','c','C','f','F','closed','filled','full',
                                 'fill','Closed','Filled','Full','Fill','FULL',
                                 'FILL','CLOSED','FILLED'},{},fillvalue='⚫')))

    def token(piece):
            if(piece in Connect4.p):
                return Connect4.p[piece]
            else:
                raise TypeError("Input Fail")
    def __init__(self,t='⚫'):
        self.B=tuple(map(copy,[["  "]*6]*7))
        self.isFilled=(Connect4.token(t) == '⚫')
    def __contains__(self,col):
        return ('  ' in self.B[col-1])
    #def __setitem__(self,key,value):
    def __setitem__(self,key,value):
        self.keys=[]
        self.values=[]
        self.keys.append(key-1)
        self.values.append(value)
        if('  ' in self.B[key-1]):
            self.B[self.keys.pop(0)][5-[*reversed(self.B[key-1])].index('  ')]=self.values.pop(0)
        else:
            raise 'This column is full\n'
    def doit(self,c,t):
        self.B[c]=t
        print(self.B)
b=Connect4('e')
b.doit(1,'⚪')
print(b.B[0])

