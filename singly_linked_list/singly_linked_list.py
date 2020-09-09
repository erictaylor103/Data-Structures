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
        #check is th head and tail have no value
        if self.head is None and self.tail is None:
            return None
        
        #get the value of the tail that we will remove
        value = self.tail.get_value()
        
        #check if there is only one item (head and tail are the same)
        #id there is only one item we will set head and tail to None
        #None will delete both tail and head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return value

        #loop through the list until we reach the tail
        current = self.head
        while current.next_node is not self.tail:
            current = current.next_node
        
        #set set the next node to None (this is the tail that we are setting to None)
        current.next_node = None
        #set the tail to None
        self.tail = None
        #move the tail to the current item
        self.tail = current
        
        #self.tail.next_node = None
        #self.tail = current

        return value