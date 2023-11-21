"""
Created on Sat Sep  3 14:44:22 2022
@author: chaoyidai
"""     
# Problem 1 phone book
class phone():
    def __init__(self, entry):
         self.command=entry[0]
         self.number=int(entry[1])
         if self.command=='add':
             self.name=entry[2]
         return 

contact={}
def entry_process(entries):
    result=[]
    if entries.command =='add':
         # if we already have contact with such number,
         # we should rewrite contact's name
         contact[entries.number]=entries.name
         
    elif entries.command =='del':
         # if we already have contact with such number,
         # we should rewrite contact's name
         contact.pop(entries.number, None)
  
    elif entries.command=='find':
         result=contact.get(entries.number,'not found')
    return result
  
    
import os
os.chdir('/Users/chaoyidai/Desktop/UCSD data structure')
with open('phone_book_input.txt','r') as f:
      data=f.readlines()
    
num=data[0].strip()    
for i in range(1,len(data)):
    entries=phone(data[i].strip().split())
    result=entry_process(entries)
    if result!=[]:
       print(result)

'''
12
add 911 police 
add 76213 Mom 
add 17239 Bob 
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy 
find 76213
'''
'''
expected output:
Mom
not found police not found Mom
daddy    
'''
    



    
# Question 2  Hashing with Chain
## Created a hash table
## Insert in the asserted location
from collections import deque
class query():
    def __init__(self, entry):
          self.command=entry[0]
          if self.command=='check':
              self.index=int(entry[1])
          else: 
              self.word=entry[1]

class entryprocessor():
    _multiplier = 263
    _prime = 1000000007
    
    def __init__(self, bucket_num):
          self.bucket_num=bucket_num
          self.hash_table=list(deque() for _ in range(bucket_num))
          
    def HashFunction(self, word):
        hash_value = 0
        for char in reversed(word):
            hash_value = (hash_value * self._multiplier + ord(char)) % self._prime
        return hash_value % self.bucket_num
    
    def processentry(self, entry):
        if entry.command == 'check':
            if self.hash_table[entry.index]:
                print(' '.join(self.hash_table[entry.index]))
            else:
                print()
        else:
            hash_value = self.HashFunction(entry.word)
            if entry.command=='add':
                if entry.word not in self.hash_table[hash_value]:
                      self.hash_table[hash_value].appendleft(entry.word)
            elif entry.command=='del':
                if entry.word in self.hash_table[hash_value]:
                      self.hash_table[hash_value].remove(entry.word)
            elif entry.command=='find':
                if entry.word in self.hash_table[hash_value]:
                      print('yes')
                else:
                      print('no')
                  
import os
os.chdir('/Users/chaoyidai/Desktop/UCSD data structure')
with open('hash_with_chain_input.txt','r')  as f:
    input=f.readlines()

bucket_num=int(input[0].strip())
command_num=int(input[1].strip())
hash_table=entryprocessor(bucket_num)
for i in range(2, len(input)):
      toy=query(input[i].strip().split())
      hash_table.processentry(toy)










## Question 3
## Generate unique index for each string        
import os
def PolyHash(string, prime, multiplier):
    hash_value = 0
    for i in range(len(string) - 1, -1, -1):
        hash_value = (hash_value*multiplier+ord(string[i]))%prime
    return hash_value

def PrecomputedHashes(sentence, word, prime, multiplier):
    t = len(sentence)
    p = len(word)
    s = text[t - p:]
    H = list([] for _ in range(t - p + 1))
    H[t - p] = PolyHash(s, prime, multiplier)
    y = 1
    for i in range(1, p + 1):
        y = (y * multiplier) % prime
    for i in range(t - p - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + p])) % prime
    return H

def RabinKarp(sentence, word):   
    t = len(sentence)
    p = len(word)
    prime = 1000000007
    multiplier = 236
    result = []
    word_hash = PolyHash(word, prime, multiplier)
    sentence_substrings = PrecomputedHashes(sentence, word, prime, multiplier)
    for i in range(t - p + 1):
        if word_hash == sentence_substrings[i]:
            result.append(i)
    return result

word = raw_input("word: ")
sentence = raw_input("sentence: ")
positions = RabinKarp(text, pattern)
for pos in positions:
    print(pos)


## Input ##
aba abacaba
## Expected Output ##
0 4


## Input ##
Test
testTesttesT
## Expected Ouput ##
4



















