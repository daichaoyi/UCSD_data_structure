#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:09:49 2022

@author: chaoyidai
"""

# Problem 1
brackets={"{":"}", "[":"]", "(":")"}
open_set={"{","[","("}
all_brackets={"{", "}", "[", "]", "(",")"}
stack=[]

def bracket_order(string):
  for index, i in enumerate(string):
      if i in open_set:
          stack.append(i)
#          print(stack)
      elif stack and i==brackets[stack[-1]]:
          stack.pop()
#          print(stack)
      elif i in all_brackets:
          return index+1
      else:
          continue
#          print(i)
  return 'Success'

string=input("input of brackets: ")

print(bracket_order(string))

'''
input: [{}]
expected output: Success

input {[}
expected output: 3

input: foo(bar)
expected output: Success

input: foo(bar[i)
expected output: 10
'''




# Problem 2 compute tree height
# input n=5
# input parents=[4,-1,4,1,1]

def tree_height(n, parents):
       nodes_depth=[None]*n
       root=parents.index(-1)
       nodes_depth[root]=1
           
# node represents nth node
# depth represents the depth of a node,           
       for node in range(n):
           depth=0
           trace=node
           
           while trace!=-1:
                trace=parents[trace]
                depth+=1
           nodes_depth[node]=depth
       return max(nodes_depth)
               
n=int(input("number of element: "))
parents=list(map(lambda x: int(x), input("list of tree: ").split()))
tree_height(n, parents)  

             
'''
input: 
5
4 -1 4 1 1
expected solution: 3

input:
 5
-1 0 4 0 3
expected solution: 4
'''
                                               




# Problem 3: Network
from collections import deque

def process_packets(packets,bufsize):
     
    # Stores the scheduled finish times for packets
    buffer = deque(maxlen=bufsize)

    start_times = [None] * len(packets)
    for i, (arrival, duration) in enumerate(packets):
        # Remove packets from the buffer that have been processed by the
        # arrival time.                   
        while buffer and buffer[0]<=arrival:
            buffer.popleft()

        if len(buffer)>=bufsize:
            # Buffer overrun
            start_times[i]=-1
        else:
            # This packet will start being processed after the finish time of
            # the last buffered packet (if there is anything in the buffer).           
            start_times[i]=max(arrival, buffer[-1] if buffer else 0)
            # Store the scheduled finish time for this packet.
            buffer.append(start_times[i]+duration)
    return start_times

bufsize=1
packets=[[0,1]]
process_packets(packets,bufsize)


                             
'''
#input
1 2 
0 1 
0 1
#expected ouput
0 
-1

#input
1 2 
0 1 
1 1
#expected output
0
1
'''


    
    
    







    
    
    
    