 ```python
from collections import defaultdict
import itertools
def find_common(a, b): # finds all possible combinations for each tree  (number should be same) eg ((1),(2)) ,((3)(4)), so will give a list like [[(x[0],y)]] and then we'll use set to remove the duplicates as usual
    return find_commonrec(a, b, [], []) # just calling recursive function with initial empty lists  for both trees values.   [(1),(2)) ,((3)(4))] will be like [[(x[0],y)], []] and then we'll use set to remove the duplicates as usual
def find_commonrec(a, b, x=None, y=None): # recursive function which checks for each element in a with every possible combination of elements from tree2 (b)   If no values are passed means it is first call so just return empty lists and then keep on passing the same as arguments till we get result
    if not b: 
        return [x, y] # when all items matched , add that to a list. this will be our base condition for recursion where each item of one tree matches with other's sub-tree or leaf node   . If no values are passed means it is first call so just return empty lists and then keep on passing the same as arguments till we get result
    if not x: # when a has items but b doesn't , add all unmatched item of 'a tree to list (these will be our final solution)  . If no values are passed means it is first call so just return empty lists and then keep on passing the same as arguments till we get result
        if isinstance(b[0], int): # when b has leaf node. compare all a's items with this single value of 'leaf-node in tree2 (in our case ((3)(4)) will be like 1,2) and then add to list which gives us solution as [[(x),y]]
            return find_commonrec(a,[b[0]], x + [None for _ in a], y+[[b[0]]*len(a)]) # here we are adding all the items from 'tree1' (in our case ((1),(2)) to list as None. This will be like  [(x),y] = [[None]*3,[4,5]]. We do this so that it can work with both leaf node and sub-trees of tree b
        else: # when a has items but b's first item is '(', means we have to recursively call our function by passing the current state as initial conditions for next recursion. i guess after reading above explanation, you should be able to understand this part too (this one was bit tricky :P)  .
            return find_commonrec(a[len(b):], b[0][1:]) + find_commonrec(a[:len(a)- len(b)], [None] * len(b)) # we are splitting 'tree2' into two parts as per the condition (eg. ((3)(4)), so will be like  [(x),y]= [[],[(5)]]. We do this because in our function definition, b is supposed to decrease from left when a doesn’t have leaf nodes but tree1 has more items than 'tree2'
    if isinstance(a[0], int): # we reached here only after comparing all possible combinations of elements. Now compare each item with first element (eg for ((3)(4)) will be 5, so this condition is met and then add to list which gives us solution as [[(x),y]]
        return find_commonrec(a[:1], b,[[a[0]]+ x, y]) +find_commonrec([None]+ a[1:],b ,[x ,  None if not isinstance (y[-1][-2] and len((set(tuple(sorted(i)) for i in find_commonrec( [e for e in itertools.chain(*a)]+ b) ) ))
def commonnodes(): # this function will take input from user, convert into required format , pass to recursive call which gives result as list of lists and then finally get the desired answer   . If no values are passed means it is first call so just return empty sets  till we don't have solution for given problem
    n = int(input()) # number if aliens (n) will be less than or equal to one lac i.e,10^5+2
    if n == -1: # this condition will be met when all items from a and b matches
        return [] # this is base case for recursion where number items from both tree1 and treen2 matches.
    elif n == 0: # this is base case for recursion where no items from tree1 and treen2 matches.
        return []  # if no items matches from both tree1 and treen2
    if not n: # this is base case for recursion where no items from tree1 and treen2 matches.
        return [] # this is base case for recursion where number items from both tree1 and treen2 matches.
    if not n: # this is base case for recursion where no items from tree1 and treen2 matches.
        return [] # this is base case for recursion where number items from both tree1 and treen2 matches.
    if not n: # this is base case for recursion where no items from tree1 and treen2 matches.
        return [] # this is base case for recursion where number items from both tree1 and treen2 matches.
    if not n: # this is base case for recursion where no items from tree1 and treen2 matches.
        return [] # this is base case for recursion where number items from both tree1 and treen2 matches.
# Generator time: 48.5165 seconds