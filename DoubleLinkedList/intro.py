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


dll = DoubleLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

dll.print_list()

dll.reverse()

dll.print_list()
