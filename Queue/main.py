class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

    
class Queue:
    def __init__(self, value):
        n = Node(value)
        self.first = n 
        self.last = n 
        self.length = 1
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.length +=1 

    def dequeue(self):
        if self.length == 0:
            return None 
        temp = self.first 
        if self.length == 1:
            self.first = None 
            self.last = None 
        else:
            self.first = self.first.next 
            temp.next = None 
        self.length -=1
        return temp 
    
    
    def print_queue(self):
        """Print the queue horizontally with first and last node indicators."""
        if self.length == 0:
            print("Queue is empty")
            return
        
        # Collect values from first to last
        values = []
        curr = self.first
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        
        # Print values with spacing
        values_str = " <- ".join(values)
        print(values_str)
        
        # Print labels for first and last
        first_label = "first"
        last_label = "last"
        
        if self.length == 1:
            # Single element is both first and last
            print("^")
            print("first/last (dequeue/enqueue)")
        else:
            # Multiple elements - show first and last separately
            # Position of first label
            first_pos = 0
            # Position of last label - estimate based on string length
            last_pos = len(values_str)
            
            print("^" + " " * (last_pos - 1) + "^")
            print("first" + " " * (last_pos - len("first") - len("last")) + "last")
            print("(dequeue)" + " " * (last_pos - len("(dequeue)") - len("(enqueue)")) + "(enqueue)")


q = Queue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_queue()

q.dequeue()
q.print_queue()
