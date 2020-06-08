"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

To run any tests you must be in the queue folder in the terminal below!!!!!!!!!!

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

#sys import for mapping to linked list
import sys
sys.path.append("../singly_linked_list") 
from singly_linked_list import LinkedList


#from linked_list import LinkedList
#import singly_linked_list
#import LinkedList
#initial code

### Queue with an array
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size    # or len(self.storage)

    def enqueue(self, value):
        self.size +=1
        # add to the back of the array 
        self.storage.append(value)  

    def dequeue(self):
         # if the size of the queue is greater than one, decrement the size
        if self.size > 0:
            self.size -= 1
            # remove from index[0] from the array
            return self.storage.pop(0)
        else:
            # if the size of the queue is zero, return None
            return None

### End queue with an array

### Queue with a LinkedList

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # increase the size of the queue by one
#         self.size += 1
#         # invoke "add_to_tail" on self.storage, passing in (item) as an argument
#         self.storage.add_to_tail(value)

#     def dequeue(self):
#         # if the size of the queue is greater than one, decrement the size
#         if self.size > 0:
#             self.size -= 1
#             # invoke "remove_head" on self.storage
#             return self.storage.remove_head()
#         else:
#             # if the size of the queue is less than or equal to zero, return None
#             return None