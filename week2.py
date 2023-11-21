#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 02:30:27 2022

@author: chaoyidai
"""

## Problem 1
class min_heap():
    def  __init__(self, array):
      self.array=array  
      self.size=len(self.array)
# swap was used to store where parents and child node exchanged value.
      self.swaps=[]
      
    def loop_over_parent_node(self):
       n=self.size
       for i in range(n//2-1, -1, -1):
           self.exchange(i)
        
# exchange the position of nodes and it's chilren node, when the value of the 
# node is higher than the children node.
    def exchange(self,i):
       min_index=i
       left_index=i*2+1
       right_index=i*2+2
       if left_index<self.size and self.array[left_index]<self.array[min_index]:
             min_index=left_index
       if right_index<self.size and self.array[right_index]<self.array[min_index]:
             min_index=right_index
       if i!=min_index:
             self.swaps.append((i, min_index))
             self.array[i],self.array[min_index]=self.array[min_index],self.array[i]
    

if __name__=="__main__":
   n=int(input("length of array:"))
   array=[int(x) for x in input("the array:").split()]
   heap=min_heap(array)
   min_heap.loop_over_parent_node(heap)
   print(heap)
   swaps = heap.swaps
   print(len(swaps))
   for swap in swaps:
     print(*swap)


         
    
# Problem 2 Parallel processing
from collections import namedtuple

def leftChild(i):
    return 2*i+1

def rightChild(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def SiftDown(i,size,data):
    maxIndex=i
    l=leftChild(i)
    print("data[maxIndex]:"+str(data[maxIndex]))
    print("maxIndex:"+str(maxIndex))
    print("l:"+str(l))
    print("size:"+str(size))
    
    if l<size and data[l]<data[maxIndex]:
        maxIndex=l
        
    r=rightChild(i)
    if r<size and data[r]<data[maxIndex]:
        maxIndex=r
    if i!=maxIndex:
        data[i],data[maxIndex]=data[maxIndex],data[i]
        SiftDown(maxIndex,size,data)

                                                
n_workers, n_jobs = [int(x) for x in input("number of worker, number of job:").split()]
jobs = [int(x) for x in input("sequence of job:").split()]
assert len(jobs) == n_jobs

data=[]

for _ in range(n_workers):
    data.append([0,_])
    
for each in jobs:
    print(data[0][1], data[0][0])
    print("data:"+str(data[0][0]))
    print("each:"+str(each))
    data[0][0]+=each
    print("data+each:"+str(data[0][0]))
    SiftDown(0,n_workers,data)      
    
    
    
''' 
## input
2 5 
1 2 3 4 5

## expected output   
0  0 
1  0 
0  1 
1  2 
0  4  
'''    



