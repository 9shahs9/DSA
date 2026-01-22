class Node:
    """Represents a single node in the linked list.
    
    Attributes:
        value: The data stored in this node.
        next: Reference to the next node in the linked list (None if this is the last node).
    """
    
    def __init__(self, value):
        """Initialize a new node with a given value.
        
        Args:
            value: The data to be stored in this node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """A singly linked list implementation.
    
    Attributes:
        head: Reference to the first node in the list.
        tail: Reference to the last node in the list.
        length: The number of nodes currently in the list.
    """
    
    def __init__(self, value):
        """Initialize a new linked list with a single node.
        
        Args:
            value: The value for the initial node.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Print all values in the linked list to the console.
        
        Traverses the entire list from head to tail and prints each node's value
        on a separate line, with "The new list is :" at the beginning and 
        "End of list" at the end.
        
        Returns:
            None
        """
        print("The new list is : ")
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print("End of list")

    def append(self, value):
        """Add a new node with the given value to the end of the list.
        
        If the list is empty, both head and tail are set to the new node.
        Otherwise, the new node is linked to the current tail, and the tail
        reference is updated. The length is always incremented by 1.
        
        Args:
            value: The value to be added to the end of the list.
            
        Returns:
            None
        """
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length += 1

    def pop(self):
        """Remove and return the value of the last node in the list.
        
        If the list is empty, returns None. If there's only one node, both head
        and tail are set to None. Otherwise, traverses to the node before the tail,
        updates the tail reference, and removes the link to the old tail.
        The length is decremented by 1 on every pop.
        
        Returns:
            The value of the last node, or None if the list is empty.
        """
        current_node = self.head
        if current_node is None:
            return None
        if current_node.next is None:
            val = current_node.value
            self.head = None
            self.tail = None
        else:
            while current_node.next != self.tail:
                current_node = current_node.next
            val = self.tail.value
            self.tail = current_node
            current_node.next = None
        self.length -= 1
        return val

    def pop_clean(self):
        """Remove and return the value of the last node using two-pointer traversal.
        
        An alternative pop implementation that uses two pointers (pre and temp)
        to traverse the list. Returns None if the list is empty. When the list
        becomes empty after popping, both head and tail are set to None.
        The length is always decremented by 1.
        
        Returns:
            The value of the last node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        """Add a new node with the given value to the beginning of the list.
        
        If the list is empty, both head and tail are set to the new node.
        Otherwise, the new node's next pointer is set to the current head,
        and the head reference is updated to the new node. The length is
        always incremented by 1.
        
        Args:
            value: The value to be added to the beginning of the list.
            
        Returns:
            None
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        """Remove and return the value of the first node in the list.
        
        Returns None if the list is empty. Updates the head reference to point
        to the next node. If the list becomes empty after the pop, the tail is
        also set to None. The length is always decremented by 1.
        
        Returns:
            The value of the first node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        pop_node = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return pop_node.value

    def get(self, idx):
        """Retrieve the node at the specified index in the list.
        
        Returns the actual Node object (not just the value) at the given index.
        Returns None if the list is empty, if the index is negative, or if the
        index is out of bounds (>= length). Indices are 0-based, where 0 refers
        to the head node.
        
        Args:
            idx: The index of the node to retrieve (0-based).
            
        Returns:
            The Node object at the specified index, or None if not found.
        """
        if self.length == 0:
            return None
        if idx < 0 or idx >= self.length:
            return None
        temp = self.head
        while idx > 0:
            temp = temp.next
            idx -= 1
        return temp
    
    def set_value(self, idx, value):
        """Set the value of the node at the specified index.
        
        Uses the get() method to locate the node at the given index, and if found,
        updates its value. Returns True if the value was successfully set, False
        otherwise (if the index is invalid or out of bounds).
        
        Args:
            idx: The index of the node to update (0-based).
            value: The new value to set at that index.
            
        Returns:
            True if the value was set successfully, False otherwise.
        """
        temp = self.get(idx)
        if temp:
            temp.value = value
            return True
        return False


    def insert(self, idx, value):
        """Insert a new node with the given value at the specified index.
        
        If the index is invalid (negative or greater than length), returns False
        without modifying the list. If the index is 0, the new node becomes the
        head. Otherwise, the new node is inserted after the node at (idx-1).
        Valid indices range from 0 to length (inclusive), where inserting at
        length appends to the end of the list. The length is always incremented
        by 1 upon successful insertion.
        
        Args:
            idx: The index at which to insert the new node (0-based).
            value: The value to be inserted.
            
        Returns:
            True if the insertion was successful, False if the index is invalid.
        """
        if idx <0 or idx > self.length:
            return False
        new_node = Node(value)
        if idx ==0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get(idx-1)
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.length +=1
        return True

