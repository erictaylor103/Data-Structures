class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node #The next node in the list
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None #Points to the first node in the list
        self.tail = None #Points to the last node in the list

    #create an add_to_tail function so we can add an item to the tail of the queue
    def add_to_tail(self, value):
        node = Node(value, None)
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    #create a remove_head function
    #what if we don;t have any nodes
    #what if there is only one node
    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        else:
            value = self.head.get_value()

        if self.tail == self.head:
            self.tail = None
        self.head = self.head.next_node

        return value

    #create a remove tail function
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        
        current = self.head
        while current.next_node is not self.tail:
            current = current.next_node
        
        value = self.tail.get_value()
        current.next_node = None
        self.tail = None
        self.tail = current
        
        #self.tail.next_node = None
        #self.tail = current

        return value