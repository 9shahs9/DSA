class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 


class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def is_empty(self):
        return self.root == None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_insert(self, curr_node, value):
        if curr_node == None:
            curr_node = Node(value)
        elif curr_node.value > value:
            curr_node.left = self.__r_insert(curr_node.left, value)
        elif curr_node.value < value:
            curr_node.right = self.__r_insert(curr_node.right, value)
        return curr_node
    
    def contains(self, value):
        if self.root == None:
            return False 
        if self.root.value == value:
            return True 
        return self.__r_contains(self.root, value)
    
    def __r_contains(self, node, value):
        if node == None:
            return False 
        if node.value > value: 
            return self.__r_contains(node.left, value)
        if node.value < value:
            return self.__r_contains(node.right, value)
        if node.value == value:
            return True 
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
    
    def __delete_node(self, curr_node, value):
        if curr_node == None:
            return None  
        if value < curr_node.value:
            curr_node.left = self.__delete_node(curr_node.left, value)
        if value > curr_node.value:
            curr_node.right= self.__delete_node(curr_node.right, value)
        if value == curr_node.value:
            #find lowest value on right sub-tree and replace it with curr node.
            if curr_node.right == None and curr_node.left == None:
                return None 
            if curr_node.left == None:
                return curr_node.right
            if curr_node.right == None:
                return curr_node.left 
            else:
                sub_tree_min = self.min_value(curr_node.right)
                curr_node.value = sub_tree_min
                curr_node.right = self.__delete_node(curr_node.right, sub_tree_min)
        return curr_node

    def min_value(self, curr_node):
        if curr_node == None:
            return None 
        while curr_node.left != None:
            curr_node = curr_node.left 
        return curr_node.value 

    def display(self):
        """Pretty print the binary search tree structure"""
        if self.is_empty():
            print("Tree is empty")
            return
        self._display_helper(self.root, "", True)
    
    def _display_helper(self, node, prefix, is_tail):
        """Recursive helper to display tree with proper formatting"""
        if node is None:
            return
        print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
        
        children = []
        if node.left:
            children.append((node.left, False))
        if node.right:
            children.append((node.right, True))
        
        for i, (child, is_right) in enumerate(children):
            is_last = (i == len(children) - 1)
            extension = "    " if is_tail else "│   "
            self._display_helper(child, prefix + extension, is_last)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(25)
bst.insert(21)
bst.insert(11)
bst.insert(14)
bst.insert(3)
bst.insert(27)
bst.insert(23)
bst.display()

bst.delete_node(20)
bst.display()


