"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev 
        self.next = next
    
    def get_data(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def get_pre(self):
        return self.prev
    
    def set_next(self, new_next):
        self.next = new_next
    
    def set_prev(self, new_prev):
        self.prev = new_prev
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.size = 1 if node is not None else 0

    def __len__(self):
        return self.size
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value=value)
        new_node.set_next(self.head)
        self.head = new_node #move the head to the new node
        self.head.prev = None #set the "prev" pointer to None (since none comes before the head)
        self.size +=1 #increment the size of the doubly linked list

        #check if the list has only 1 node
        #if there's only one node, set the tail to the head also
        if self.size == 1:
            self.tail = self.head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        temp = self.head

        if self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -=1
        
            if self.size == 0:
                self.tail = None
            
            return temp.value
        
        else:
            self.head = None
            self.tail = None
            self.size -=1

            return temp.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, data):
        new_node = ListNode(value=data)
        current = self.head

        if self.size == 0:
            self.head = new_node
            self.tail = self.head
        
        else:
            while current.next is not None:
                current = current.next
            current.set_prev(current)
            current.set_next(new_node)
            self.tail = new_node
        self.tail.next = None
        #if there is a current -> if the new_node exists
        if current:
            self.tail.prev = current.prev
        else:
            self.tail.prev = None
        self.size +=1
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        temp = self.tail

        if self.size > 1:
            self.tail.next = None
            self.size -=1

            if self.size == 0:
                self.tail = None
            
            return temp.value
        
        else:
            self.head = None
            self.tail = None
            self.size -=1

            return temp.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head
        if current == node:
            pass
        else:
            node.set_next(current)
            node.set_prev(None)
            self.head = node

            if self.size == 1:
                self.tail = self.head
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return

        value = node.value

        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.size -= 1
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        if current is None or node is None:
            return
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        while node is not current: #check if the syntax is correct
            current = current.next
        if current == node:
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
        
        self.size -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self, start=None):
        if not self.head:
            return None
        max_val = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_val:
                max_val = current_node.value
            
            #increment
            current_node = current_node.next
        
        return  max_val
        


#myList = DoublyLinkedList()
#myList.add_to_head(1)
#myList.add_to_head(2)
#myList.add_to_head(3)
#print(myList)