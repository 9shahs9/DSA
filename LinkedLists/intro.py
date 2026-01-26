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
        """Print the linked list in a visual format showing links between nodes.
        
        Displays the list as: value1 -> value2 -> value3 -> None
        For an empty list, displays: None
        
        Returns:
            None
        """
        if self.head is None:
            print("None")
            return
        
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.value))
            temp = temp.next
        
        print(" -> ".join(result) + " -> None")

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
        return temp

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
        return pop_node

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
    
    def remove(self, idx):
        if idx <0 or idx >= self.length:
            return None
        if idx == 0:
            return self.pop_first()
        if idx == self.length - 1:
            return self.pop_clean()
        prev_node = self.get(idx-1)
        return_node = prev_node.next
        prev_node.next = return_node.next
        self.length -= 1
        return_node.next = None
        return return_node
    
    def reverse(self):
        if self.length <= 1:
            return True
        op_node = self.head
        prev_node = self.head.next
        curr_node = self.head.next 
        self.head.next = None 
        if curr_node.next is None:
            prev_node.next = op_node
        else:
            while curr_node.next :
                prev_node = curr_node
                curr_node = curr_node.next 
                prev_node.next = op_node
                op_node = prev_node
            curr_node.next = prev_node
        temp = self.head 
        self.head = self.tail
        self.tail = temp
        return True
    
    def make_empty(self):
        self.head = None 
        self.tail = None 
        self.length = 0

    def leet_code_find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast != None and fast != self.tail:
            slow = slow.next
            if fast.next == None or fast.next.next == None:
                break
            fast = fast.next.next
        return slow

    def leet_code_has_loop(self):
        fast = self.head
        slow = self.head
        while (fast != None):
            slow = slow.next
            if (fast.next == None or fast.next.next == None):
                return False
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def leet_code_find_kth_from_end(self, k):
        fast = self.head
        slow = self.head
        for _ in range(k-1):
            if fast == self.tail:
                return None
            if fast.next:
                fast = fast.next
        while fast != self.tail:
            fast = fast.next
            slow = slow.next
        return slow

    def leet_code_remove_duplicates(self):
        seen = set()
        prev = self.head
        curr = self.head
        while(curr != None):
            if curr.value in seen:
                prev.next = curr.next
            else:
                seen.add(curr.value)
                prev = curr
            curr = curr.next

    def leet_code_remove_duplicate_nested(self):
        curr = self.head
        while curr != None:
            runner = curr
            while runner.next != None:
                if curr.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next

    def leet_code_binary_to_decimal(self):
        length = 0
        curr = self.head
        while curr!=None:
            length +=1
            curr = curr.next

        value = 0
        curr = self.head
        while curr!=None:
            value += (2**(length-1))*curr.value
            length -=1
            curr = curr.next
        return value
    

    """
LL: Partition List ( ** Interview Question)
LeetCode #86 (Adapted)



⚠️ CAUTION: Advanced Challenge Ahead!

This Linked List problem is significantly more challenging than the ones we've tackled so far. It's common for students at this stage to find this exercise demanding, so don't worry if you're not ready to tackle it yet. It's perfectly okay to set it aside and revisit it later when you feel more confident.

If you decide to take on this challenge, I strongly advise using a hands-on approach: grab a piece of paper and visually map out each step.

This problem requires a clear understanding of how elements in a Linked List interact and move. By now, you've observed numerous Linked List animations in the course, which have prepared you for this moment.

This exercise will be a true test of your ability to apply those concepts practically. Remember, patience and persistence are key here!

Now, here is the exercise:

___________________________________



Implement the partition_list member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.

Note:  This linked list class does NOT have a tail which will make this method easier to implement.

The original relative order of the nodes should be preserved.



Details:

The function partition_list takes an integer x as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.



Example 1:

Input:

Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5

Process:

Values less than 5: 3, 2, 1

Values greater than or equal to 5: 8, 5, 10

Output:

Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10





Example 2:
Input:

Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3

Process:

Values less than 3: 1, 2, 2

Values greater than or equal to 3: 4, 3, 5

Output:

Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5





Tips:

While traversing the linked list, maintain two separate chains: one for values less than x and one for values greater than or equal to x.

Use dummy nodes to simplify the handling of the heads of these chains.

After processing the entire list, connect the two chains to get the desired arrangement.



Note:

The solution must maintain the relative order of nodes. For instance, in the first example, even though 8 appears before 5 in the original list, the partitioned list must still have 8 before 5 as their relative order remains unchanged.

Note:

You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' next pointers may be changed.)

/Constraints : This method can't use tail member variable. 
    
    """

    def leet_code_partition_list(self, x):
        left_init = 0
        right_init = 0
        curr = self.head
        if curr == None:
            return 
        while(curr != None):
            if curr.value < x:
                if left_init == 0:
                    left = LinkedList(curr.value)
                    left_init = 1 
                else: 
                    left.append(curr.value)
            else:
                if right_init == 0:
                    right = LinkedList(curr.value)
                    right_init = 1 
                else:
                    right.append(curr.value)
            curr = curr.next 
        self.make_empty()
        if left_init == 1:
            cleft = left.head
            while (cleft != None ):
                self.append(cleft.value)
                cleft = cleft.next
        if right_init == 1:
            cr = right.head
            while cr!= None :
                self.append(cr.value)
                cr = cr.next 


    def leet_code_partition_list_dummy_nodes(self, x):
        d1 = Node(0)
        d2 = Node(0)
        pd1 = d1 
        pd2 = d2 
        curr = self.head 
        while(curr != None):
            if (curr.value < x):
                pd1.next = curr 
                pd1 = pd1.next 
            else:
                pd2.next = curr
                pd2 = pd2.next  
            curr = curr.next
        pd1.next = None 
        pd2.next = None  
        pd1.next = d2.next 
        self.head = d1.next


    def leet_code_reverse_between(self, st_idx, end_idx):
        """ Key assumptions: 
        1. No length attribute available. 
        2. No tail attribute available. 
        3. st_idx and end_idx would be within bounds
        4. can't use self.get """
        
        ' Code all exceptions here '
        if self.head == None or self.head.next == None:
            return 
        'dummy node'
        d1 = Node(0)
        d1.next = self.head 

        prev = d1 
        curr = self.head 
        move_node = self.head.next

        for i in range(st_idx):
            prev = curr 
            curr = curr.next 
            move_node = curr.next 
        
        for _ in range(end_idx - st_idx):
            curr.next = move_node.next 
            move_node.next = prev.next 
            prev.next = move_node
            move_node = curr.next
        
        self.head = d1.next 
        return 


            


        
        
        

