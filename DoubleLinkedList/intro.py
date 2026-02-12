class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:

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
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True 

    def pop(self):
        if self.length == 0:
            return None 
        ret_node = self.tail
        self.length -=1 
        if self.length == 0:
            self.head = None 
            self.tail = None 
        else:
            self.tail = self.tail.prev
            self.tail.next = None 
            ret_node.prev = None 
        return ret_node 
        
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.length +=1
        if self.length == 1:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        return True 
        
    
    def pop_first(self):
        ret_node = self.head 
        if self.length == 0:
            return None 
        self.length -=1 
        if self.length == 0:
            self.head = None 
            self.tail = None 
        else: 
            self.head = self.head.next 
            self.head.prev = None 
        ret_node.next = None
        return ret_node

    
    def get(self, idx):
        if idx <0 or idx >= self.length:
            return None 
        curr = self.head 
        for _ in range(idx):
            curr = curr.next 
        return curr 
    
    def set(self, idx, value):
        node = self.get(idx)
        if node is None:
            return False 
        node.value = value 
        return True 

    def insert(self, idx, value):
        node = Node(value)
        if idx <0 or idx > self.length:  #Validate the condition here later.
            return False
        if idx == self.length:
            return self.append(value)
        if idx == 0:
            return self.prepend(value)
        
        prev = self.get(idx-1)
        node.prev = prev 
        node.next = prev.next 
        prev.next = node 
        node.next.prev = node 
        self.length += 1
        return True 

    
    def remove(self, idx):
        if idx <0 or idx >= self.length:
            return None 
        prev = self.head 
        if idx == 0:  #remove head case. 
            return self.pop_first()
        if idx == self.length - 1:
            return self.pop()

        for _ in range(idx-1):
            prev = prev.next 
        curr = prev.next 
        prev.next = curr.next 
        curr.next.prev = prev 
        curr.next = None 
        curr.prev = None 
        self.length -= 1
        return curr 
            

        



    def reverse(self):
        temp = None
        current_node = self.head
        while current_node:
            temp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp
            current_node = current_node.prev
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
