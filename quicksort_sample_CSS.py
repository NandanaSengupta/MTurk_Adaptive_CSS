
# coding: utf-8

# In[1]:

from random import randrange
from random import sample

# given list, sub-list (defined by start and end indices), random pivot index
def partition(lst, start, end, pivot):
    # place pivot at the end of the sub-list
    lst[pivot], lst[end] = lst[end], lst[pivot]
    lst_below_pivot = []
    lst_above_pivot = []
    query_counter = 0 
    
    # dividing into two lists (above and below pivot)
    for i in range(start, end):
        query_counter +=1 
        if lst[i] < lst[end]:
              lst_below_pivot.append(lst[i])
        if lst[i] >= lst[end]:
              lst_above_pivot.append(lst[i])
    
    next_pivot = start + len(lst_below_pivot)
    
    lst[start : next_pivot ] = lst_below_pivot
    lst[next_pivot] = lst[end]
    lst[(next_pivot + 1): end+1 ] = lst_above_pivot

    return next_pivot, query_counter

def quick_sort(lst, start, end):
    if start >= end:
        return 0
    pivot = randrange(start, end + 1)
    new_pivot, nqueries = partition(lst, start, end, pivot)
    nqueries += quick_sort(lst, start, new_pivot - 1)
    nqueries += quick_sort(lst, new_pivot + 1, end)
    return nqueries

def sort(lst):
    nqueries = quick_sort(lst, 0, len(lst) - 1)
    return nqueries


# In[4]:

from copy import deepcopy

lst = sample( range(1000), 100)
lstcopy = deepcopy(lst)
total_queries = sort(lst)  


# In[ ]:

print "original list:" , lstcopy , "\n" 
print "sorted list:", lst , "\n\n" 

print "total number of items = " , len(lst)
print "total non-adaptive queries required = n(n-1)/2 = " , len(lst)*(len(lst)-1)/2
print "total quicksort queries = " , total_queries
     

