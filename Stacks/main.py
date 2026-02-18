class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Stack:
    def __init__(self, value):
        curr = Node(value)
        self.top = curr
        self.height = 1

    def is_empty(self):
        return self.height == 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.top == None:
            return None 
        ret_node = self.top 
        self.top = self.top.next
        ret_node.next = None
        self.height -= 1
        return ret_node.value
    
    def peek(self):
        if self.top == None:
            return None 
        return self.top.value 
    
    def print_horizontal(self):
        """Print the stack horizontally with top pointer indicator."""
        if self.top is None:
            print("Stack is empty")
            return
        
        # Collect values from top to bottom
        values = []
        curr = self.top
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        
        # Print values with spacing
        values_str = " <- ".join(values)
        print(values_str)
        
        # Print pointer to top
        print("^")
        print("top")


def sort_stack(input_stack ):
    if input_stack.is_empty():
        return True
    staging = Stack(input_stack.pop())
    while not input_stack.is_empty():
        temp = input_stack.pop()
        while staging.peek() and temp < staging.peek():
            input_stack.push(staging.pop())
        staging.push(temp)
    while not staging.is_empty():
        input_stack.push(staging.pop())

if __name__ == "__main__":
    s = Stack(2)
    s.push(4)
    s.push(3)
    s.push(1)
    sort_stack(s)
    s.print_horizontal()
    