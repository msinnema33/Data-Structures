"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

To run any tests you must be in the stack folder in the terminal below!!!!!!!!!!

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

#sys import for mapping to linked list
import sys
sys.path.append("../singly_linked_list") 
from singly_linked_list import LinkedList


# ###implement using an array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)
        

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         return self.storage.pop()

# ### End with array

### Implement using a linked list

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # temp = self.head
        # count = 0

        # while (temp):
        #     count += 1
        #     temp = temp.next
        # return count
        return self.size

    def getCount(self):
        temp = self.head
        count = 0

        while (temp):
            count += 1
            temp = temp.next
        return count
        
    def push(self, value):
        # increase the size of the queue by one
        self.size += 1
        # invoke "add_to_tail" on self.storage, passing in (item) as an argument
        self.storage.add_to_tail(value)

    def pop(self):
        ## remove from the top(tail) of the stack
        if self.size > 0:
            self.size -= 1
            # invoke "remove_head" on self.storage
            return self.storage.remove_tail()
        else:
            # if the size of the queue is less than or equal to zero, return None
            return None

        
