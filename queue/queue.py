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

import sys
sys.path.append("/Users/erictaylor/Documents/Lambda/Data-Structures/singly_linked_list/")
from singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        #initialize the "size" to keep track of how big the queue is
        self.size = 0
        #set the "storage" to the LinkedList()
        self.storage = LinkedList()
    
    def __len__(self):
        #get the length of the size and return it
        return self.size

    def enqueue(self, value):
        #increment the size by 1
        self.size +=1
        #call the add_to_tail method from the storage (LinkedList)
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -=1
        return self.storage.remove_head()

    def print_list(self):
        current_node = self.storage.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next_node

queue = Queue()
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)

queue.dequeue()
queue.print_list()
