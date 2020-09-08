class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node #The next node in the list

class LinkedList:
    def __init__(self):
        self.head = None #Points to the first node in the list
        self.tail = None #Points to the last node in the list
    
    def add_to_tail(self, value):
        new_tail = Node(value, None)
        
        if not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next_node = new_tail
            self.tail = new_tail
            #old_tail = self.tail
            #old_tail = new_tail

    def remove_head(self):
        pass

    def remove_tail(self):
        pass