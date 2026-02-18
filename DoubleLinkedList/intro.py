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

    def make_empty(self):
        self.head = None 
        self.tail = None 
        self.length = 0

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


    def is_palindrome(self):
        forward = self.head
        backward = self.tail 
        if (self.length == 0):
            return True
        for _ in range(self.length // 2):
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
        return True 
    
    def partition_list(self, x):
        left_init = False
        right_init = False
        curr = self.head
        while curr:
            if curr.value < x:
                if left_init:
                    left_dl.append(curr.value)
                else:
                    left_dl = DoubleLinkedList(curr.value)
                    left_init = True
            else:
                if right_init:
                    right_dl.append(curr.value)
                else:
                    right_dl = DoubleLinkedList(curr.value)
                    right_init = True 
            curr = curr.next 
        self.make_empty()
        if left_init:
            left_curr = left_dl.head
            while left_curr:
                self.append(left_curr.value)
                left_curr = left_curr.next
        if right_init:
            right_curr = right_dl.head
            while right_curr:
                self.append(right_curr.value)
                right_curr = right_curr.next
        
    def partition_list_dummy_nodes(self, x):
        l_dummy = Node(0)
        r_dummy = Node(0)
        d1 = l_dummy
        d2 = r_dummy
        curr = self.head 
        while curr:
            if curr.value < x:
                l_dummy.next = curr 
                curr.prev = l_dummy
                l_dummy = curr 
            else:
                r_dummy.next = curr 
                curr.prev = r_dummy
                r_dummy = curr
            curr = curr.next
        r_dummy.next = None
        l_dummy.next = d2.next 
        if d2.next:
            d2.next.prev = l_dummy
        self.head = d1.next 
        # Set tail to the last node of right partition if it exists, otherwise last of left
        self.tail = r_dummy if d2.next else l_dummy
        if self.head:
            self.head.prev = None

        
        
def _values_forward(dll):
    values = []
    curr = dll.head
    while curr is not None:
        values.append(curr.value)
        curr = curr.next
    return values

def _values_backward(dll):
    values = []
    curr = dll.tail
    while curr is not None:
        values.append(curr.value)
        curr = curr.prev
    return values

if __name__ == "__main__":
    dll = DoubleLinkedList(3)
    dll.append(5)
    dll.append(8)
    dll.append(5)
    dll.append(10)
    dll.append(2)
    dll.append(1)
    dll.partition_list_dummy_nodes(5)
    values = _values_forward(dll)
    assert values == [3, 2, 1, 5, 8, 5, 10]
    value = _values_backward(dll)
    assert values == [10,5,8,5,1,2,3]

