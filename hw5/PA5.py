from random import randrange as rnd
from functools import reduce, partial
from itertools import zip_longest
from operator import concat, eq, mul
from collections import ChainMap
from copy import copy
from random import randrange as rnd
from numpy import transpose,array
isFilled = True

B=tuple(map(lambda x: [copy(x)]*6,["  "]*7))
emptyNames=frozenset({'E','e','Empty','empty','EMPTY','H','h','Hollow','hollow','HOLLOW','O','o','Open','open','OPEN','⚪'})
fullNames=frozenset({'F','f','Full','full','FULL','Filled','filled','FILLED','Fill','fill','FILL','c','C','Closed','closed','CLOSED','⚫'})
piece=ChainMap(dict(zip_longest(emptyNames,'⚪',fillvalue='⚪')),dict(zip_longest(fullNames,'⚫',fillvalue='⚫')))

def drop(*moves, player='Auto', toggle=True, **kws):
    global isFilled
    moves=list(moves)
    n=kws["numMoves"] if "numMoves" in kws else len(moves) if len(moves) else 1

    for l in range(n):
        token = '⚪⚫'[isFilled] if player=='Auto' else piece[player]
        if len(moves) == 0:
            try:
                moves=[int((y:=reduce(concat,map(str,(filter(None,map(mul,map(eq,array(B).transpose()[0],['  ']*6),range(1,8)))))))[rnd(len(y))])]
            except:
                if "announce" in kws:
                    print("The board's full, so",token,"can't randomly place.")
                return False
        c=moves.pop(0)
        if '  ' not in B[c-1]:
            if "announce" in kws:
                print(token,"was unable to place into column",str(c)+".")
            return False
        if "announce" in kws:
            print(token,"places into column",str(c)+".")
        B[c-1][5-[*reversed(B[c-1])].index('  ')]=token
        if toggle: isFilled ^=1

def display():
    printrow=partial(print,'',sep="|",end="|\n")
    r=tuple(zip(*B))
    print("┌──┬──┬──┬──┬──┬──┬──┐")
    for i in range(6):
        printrow(*r[i])
        if i==5: break
        print("├──┼──┼──┼──┼──┼──┼──┤")
    print("└──┴──┴──┴──┴──┴──┴──┘")
    
drop(1,toggle=False,announce=True)
drop(1,toggle=False,announce=True)
drop(1,announce=True)
drop(1,toggle=False,announce=False)
drop(7,player='⚫',toggle=False,announce=False)
drop(7,toggle=False,announce=False)
drop(7,toggle=False,announce=False)
drop(7,player='⚫',announce=False)
drop(7,player='⚫',announce=False)
drop(7,player='⚫',announce=False)
display()
drop(2,3,4,5,6,announce=True)
drop(2,3,4,5,6,toggle=False,announce=True)
drop(2,3,4,5,6,player="empty",announce=True)
drop(2,3,4,5,6,player="Filled",announce=True)
display()
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
drop(announce=True)
display()
