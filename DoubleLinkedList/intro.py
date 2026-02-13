class Node:
    """Node with value and bidirectional links."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    """Doubly linked list with head, tail, and length."""

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        print("The new list is : ")
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print("End of list")

    def append(self, value):
        """Add node to end, maintaining both links."""
        new_node = Node(value)
        if self.head is None:  # empty list
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True 

    def pop(self):
        """Remove and return last node."""
        if self.length == 0:
            return None 
        ret_node = self.tail
        self.length -= 1 
        if self.length == 0:  # last node
            self.head = None 
            self.tail = None 
        else:
            self.tail = self.tail.prev
            self.tail.next = None 
            ret_node.prev = None 
        return ret_node 
        
    
    def prepend(self, value):
        """Add node to front."""
        new_node = Node(value)
        new_node.next = self.head
        self.length += 1
        if self.length == 1:  # first in list
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        return True 
        
    
    def pop_first(self):
        """Remove and return first node."""
        ret_node = self.head 
        if self.length == 0:
            return None 
        self.length -= 1 
        if self.length == 0:  # last node
            self.head = None 
            self.tail = None 
        else: 
            self.head = self.head.next 
            self.head.prev = None 
        ret_node.next = None
        return ret_node

    
    def get(self, idx):
        """Return node at index or None."""
        if idx < 0 or idx >= self.length:
            return None 
        if idx < self.length/2:
            curr = self.head 
            for _ in range(idx):
                curr = curr.next 
        else:
            curr = self.tail 
            for _ in range(self.length - idx - 1):
                curr = curr.prev 
        return curr 
    
    def set(self, idx, value):
        """Update value at index."""
        node = self.get(idx)
        if node is None:
            return False 
        node.value = value 
        return True 

    def insert(self, idx, value):
        """Insert node at index."""
        node = Node(value)
        if idx < 0 or idx > self.length:  # invalid range
            return False
        if idx == self.length:  # append case
            return self.append(value)
        if idx == 0:  # prepend case
            return self.prepend(value)
        
        # middle insertion: link both directions
        prev = self.get(idx - 1)
        node.prev = prev 
        node.next = prev.next 
        prev.next = node 
        node.next.prev = node 
        self.length += 1
        return True 

    
    def remove(self, idx):
        """Remove and return node at index."""
        if idx < 0 or idx >= self.length:
            return None 
        prev = self.head 
        if idx == 0:  # remove head
            return self.pop_first()
        if idx == self.length - 1:  # remove tail
            return self.pop()

        # middle removal: unlink and reconnect both directions
        for _ in range(idx - 1):
            prev = prev.next 
        curr = prev.next 
        prev.next = curr.next 
        curr.next.prev = prev 
        curr.next = None 
        curr.prev = None 
        self.length -= 1
        return curr 
            
    def reverse(self):
        """Reverse list by swapping next/prev pointers."""
        temp = None
        current_node = self.head
        while current_node:  # swap pointers for each node
            temp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp
            current_node = current_node.prev
        # swap head and tail
        t = self.head
        self.head = self.tail
        self.tail = t


if __name__ == "__main__":
    dll = DoubleLinkedList(1)
    dll.append(3)
    dll.insert(1,2)
    dll.print_list()
    node2 = dll.get(1)
    print(node2.value )
    print(node2.prev == dll.head)
    print(node2.next is dll.tail)
    print(dll.head.next is node2)
    print(dll.tail.prev is node2)
