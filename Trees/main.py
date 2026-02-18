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
        new_node = Node(value)
        if self.is_empty():
            self.root = new_node 
            return 
        curr_node = self.root
        done = False 
        while ( not done):
            if curr_node.value > value: 
                if curr_node.left:
                    curr_node = curr_node.left 
                else:
                    curr_node.left = new_node
                    done = True 
            else:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = new_node
                    done = True
    
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



tree = BinarySearchTree()
l = [47, 21, 76, 18, 52, 82, 27]
for v in l:
    tree.insert(v)
tree.display()
