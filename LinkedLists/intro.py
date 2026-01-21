class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length +=1
        
    def pop(self):
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
        self.length -=1
        return val


ll = LinkedList(4)
ll.append(10)
print(ll.print_list())
ll.pop()
print(ll.print_list())
ll.pop()
print(ll.print_list())
ll.pop()
print(ll.print_list())