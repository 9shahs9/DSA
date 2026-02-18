class Node:
    """Single linked-list node."""
    
    def __init__(self, value):
        """Create a node with a value and no next."""
        self.value = value
        self.next = None


class LinkedList:
    """Singly linked list with head, tail, and length."""
    
    def __init__(self, value):
        """Create a list with one node."""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Print values as v1 -> v2 -> ... -> None."""
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
        """Add a node to the end."""
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length += 1

    def pop(self):
        """Remove and return the last value."""
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
        """Pop using two pointers; return the last node."""
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
        """Add a node to the front."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        """Remove and return the first node."""
        if self.length == 0:
            return None
        pop_node = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return pop_node

    def get(self, idx):
        """Return the node at index, or None."""
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
        """Set value at index; return success."""
        temp = self.get(idx)
        if temp:
            temp.value = value
            return True
        return False


    def insert(self, idx, value):
        """Insert value at index; return success."""
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
        """Reverse sublist from st_idx to end_idx (inclusive)."""

        if self.head == None or self.head.next == None:
            return 
        # Dummy node to simplify head changes.
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
    

    def swap_pairs(self):
        if self.head == None or self.head.next == None: 
            return
        
        dummy = Node(0)  # Dummy node to simplify head changes
        dummy.next = self.head
        prev = dummy
        curr = self.head
        
        while curr and curr.next:
            # Nodes to be swapped
            first = curr
            second = curr.next
            
            # Swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move to next pair
            prev = first
            curr = first.next
        
        self.head = dummy.next
        
        # Update tail
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        self.tail = curr

