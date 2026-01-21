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
        print("The new list is : ")
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next
        print("End of list")

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
    

    def pop_clean(self):
        if self.length == 0:
            return None 
        temp = self.head
        pre=self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre 
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None 
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1


    def pop_first(self):
        if self.length == 0:
            return None
        pop_node = self.head
        self.head = self.head.next
        self.length -=1
        return pop_node.value
    

        
        
        



ll = LinkedList(4)
ll.append(10)
print(ll.print_list())

ll.pop_clean()
print(ll.print_list())
ll.prepend(20)
print(ll.print_list())

print(ll.pop_first())
print(ll.print_list())

