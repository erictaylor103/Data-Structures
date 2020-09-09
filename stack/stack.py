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

"""
#implement the Stack using an array as the storage structure
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items

#test the stack functionality with an array
s = Stack()
s.push("A")
s.push("B")
print(s.get_stack())
"""


#####implement the Stack using linked list as the storage structure
import sys
sys.path.append("/Users/erictaylor/Documents/Lambda/Data-Structures/singly_linked_list/")
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size +=1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        return None

        