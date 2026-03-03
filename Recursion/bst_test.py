import pytest
from bst import Node, BinarySearchTree


class TestNodeInitialization:
    """Test cases for Node initialization."""
    
    def test_node_creation(self):
        """Test creating a node with a value."""
        node = Node(10)
        assert node.value == 10
        assert node.left is None
        assert node.right is None
    
    def test_node_with_different_values(self):
        """Test creating nodes with different data types."""
        node1 = Node(5)
        node2 = Node(100)
        node3 = Node(-50)
        
        assert node1.value == 5
        assert node2.value == 100
        assert node3.value == -50


class TestBSTInitialization:
    """Test cases for BST initialization."""
    
    def test_bst_creation(self):
        """Test creating an empty BST."""
        bst = BinarySearchTree()
        assert bst.root is None
    
    def test_is_empty_on_new_tree(self):
        """Test that new tree is empty."""
        bst = BinarySearchTree()
        assert bst.is_empty() is True


class TestBSTInsert:
    """Test cases for insert operation."""
    
    def test_insert_into_empty_tree(self):
        """Test inserting first element."""
        bst = BinarySearchTree()
        bst.insert(10)
        
        assert bst.root is not None
        assert bst.root.value == 10
        assert not bst.is_empty()
    
    def test_insert_multiple_elements(self):
        """Test inserting multiple elements."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        
        assert bst.root.value == 10
        assert bst.root.left.value == 5
        assert bst.root.right.value == 15
    
    def test_insert_maintains_bst_property(self):
        """Test that BST property is maintained."""
        bst = BinarySearchTree()
        values = [10, 5, 15, 3, 7, 12, 20]
        for val in values:
            bst.insert(val)
        
        # Verify BST property
        assert bst.root.value == 10
        assert bst.root.left.value == 5
        assert bst.root.right.value == 15
        assert bst.root.left.left.value == 3
        assert bst.root.left.right.value == 7
        assert bst.root.right.left.value == 12
        assert bst.root.right.right.value == 20
    
    def test_insert_duplicate_values(self):
        """Test inserting duplicate values."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(10)  # Duplicate
        
        # Duplicates are ignored in BST
        assert bst.root.value == 10
        assert bst.root.left is None
        assert bst.root.right is None


class TestBSTContains:
    """Test cases for contains operation."""
    
    def test_contains_root_element(self):
        """Test finding root element."""
        bst = BinarySearchTree()
        bst.insert(10)
        
        assert bst.contains(10) is True
    
    def test_contains_existing_elements(self):
        """Test finding existing elements."""
        bst = BinarySearchTree()
        values = [10, 5, 15, 3, 7, 12, 20]
        for val in values:
            bst.insert(val)
        
        for val in values:
            assert bst.contains(val) is True
    
    def test_contains_non_existent_element(self):
        """Test searching for non-existent element."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        
        assert bst.contains(100) is False
        assert bst.contains(1) is False
    
    def test_contains_in_empty_tree(self):
        """Test searching in empty tree."""
        bst = BinarySearchTree()
        
        assert bst.contains(10) is False


class TestBSTDeleteNode:
    """Test cases for delete_node operation."""
    
    def test_delete_from_empty_tree(self):
        """Test deleting from empty tree."""
        bst = BinarySearchTree()
        result = bst.delete_node(10)
        
        assert result is None
        assert bst.is_empty()
    
    def test_delete_non_existent_node(self):
        """Test deleting non-existent node."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        
        bst.delete_node(100)
        
        # Tree should remain unchanged
        assert bst.contains(10) is True
        assert bst.contains(5) is True
        assert bst.contains(15) is True
    
    def test_delete_leaf_node(self):
        """Test deleting a leaf node (no children)."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        
        bst.delete_node(5)
        
        assert bst.contains(5) is False
        assert bst.contains(10) is True
        assert bst.contains(15) is True
    
    def test_delete_node_with_right_child_only(self):
        """Test deleting node with only right child."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(20)
        
        bst.delete_node(15)
        
        assert bst.contains(15) is False
        assert bst.contains(20) is True
        assert bst.root.right.value == 20
    
    def test_delete_node_with_left_child_only(self):
        """Test deleting node with only left child."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(12)
        
        bst.delete_node(15)
        
        assert bst.contains(15) is False
        assert bst.contains(12) is True
        assert bst.root.right.value == 12
    
    def test_delete_node_with_two_children(self):
        """Test deleting node with two children."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        
        bst.delete_node(15)
        
        assert bst.contains(15) is False
        assert bst.contains(10) is True
        assert bst.contains(5) is True
        assert bst.contains(20) is True
        assert bst.contains(12) is True
    
    def test_delete_root_node_no_children(self):
        """Test deleting root when it has no children."""
        bst = BinarySearchTree()
        bst.insert(10)
        
        bst.delete_node(10)
        
        assert bst.root is None
        assert bst.is_empty()
    
    def test_delete_root_node_with_right_child(self):
        """Test deleting root with only right child."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(15)
        bst.insert(20)
        
        bst.delete_node(10)
        
        assert bst.root.value == 15
        assert bst.contains(10) is False
    
    def test_delete_root_node_with_left_child(self):
        """Test deleting root with only left child."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(3)
        
        bst.delete_node(10)
        
        assert bst.root.value == 5
        assert bst.contains(10) is False
    
    def test_delete_root_node_with_two_children(self):
        """Test deleting root with two children."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        
        bst.delete_node(10)
        
        assert bst.contains(10) is False
        assert bst.contains(5) is True
        assert bst.contains(15) is True
        assert bst.root is not None
    
    def test_delete_maintains_bst_property(self):
        """Test that BST property is maintained after deletion."""
        bst = BinarySearchTree()
        values = [10, 5, 15, 3, 7, 12, 20]
        for val in values:
            bst.insert(val)
        
        bst.delete_node(5)
        
        # Verify remaining elements and BST property
        for val in [10, 15, 3, 7, 12, 20]:
            assert bst.contains(val) is True
    
    def test_delete_multiple_nodes(self):
        """Test deleting multiple nodes sequentially."""
        bst = BinarySearchTree()
        values = [10, 5, 15, 3, 7, 12, 20]
        for val in values:
            bst.insert(val)
        
        bst.delete_node(3)
        bst.delete_node(7)
        bst.delete_node(12)
        
        assert bst.contains(3) is False
        assert bst.contains(7) is False
        assert bst.contains(12) is False
        assert bst.contains(10) is True
        assert bst.contains(5) is True
        assert bst.contains(15) is True
        assert bst.contains(20) is True
    
    def test_delete_all_nodes(self):
        """Test deleting all nodes from tree."""
        bst = BinarySearchTree()
        values = [10, 5, 15]
        for val in values:
            bst.insert(val)
        
        for val in values:
            bst.delete_node(val)
        
        assert bst.root is None
        assert bst.is_empty()
    
    def test_delete_node_with_complex_subtree(self):
        """Test deleting node with complex subtree."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
        for val in values:
            bst.insert(val)
        
        bst.delete_node(30)
        
        assert bst.contains(30) is False
        # Verify other nodes are intact
        for val in [50, 70, 20, 40, 60, 80, 10, 25, 35, 65]:
            assert bst.contains(val) is True
    
    def test_delete_and_reinsert(self):
        """Test deleting and reinserting the same value."""
        bst = BinarySearchTree()
        values = [10, 5, 15, 3, 7]
        for val in values:
            bst.insert(val)
        
        bst.delete_node(5)
        assert bst.contains(5) is False
        
        bst.insert(5)
        assert bst.contains(5) is True
    
    def test_delete_with_right_subtree(self):
        """Test deleting node whose inorder successor has right child."""
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(30)
        bst.insert(70)
        bst.insert(20)
        bst.insert(40)
        bst.insert(60)
        bst.insert(80)
        bst.insert(65)
        
        bst.delete_node(50)
        
        assert bst.contains(50) is False
        # Check all other values are still present
        for val in [30, 70, 20, 40, 60, 80, 65]:
            assert bst.contains(val) is True


class TestBSTIntegration:
    """Integration tests for BST operations."""
    
    def test_insert_delete_sequence(self):
        """Test a sequence of inserts and deletes."""
        bst = BinarySearchTree()
        
        # Insert values
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        assert bst.contains(10) is True
        
        # Delete and verify
        bst.delete_node(5)
        assert bst.contains(5) is False
        
        # Insert and verify
        bst.insert(3)
        assert bst.contains(3) is True
        
        # Delete root
        bst.delete_node(10)
        assert bst.contains(10) is False
    
    def test_large_tree_deletion(self):
        """Test deletion in a larger tree."""
        bst = BinarySearchTree()
        values = list(range(1, 16))
        
        for val in values:
            bst.insert(val)
        
        # Delete middle values
        bst.delete_node(8)
        bst.delete_node(5)
        bst.delete_node(12)
        
        # Verify deletions and remaining values
        assert bst.contains(8) is False
        assert bst.contains(5) is False
        assert bst.contains(12) is False
        
        for val in [1, 2, 3, 4, 6, 7, 9, 10, 11, 13, 14, 15]:
            assert bst.contains(val) is True
    
    def test_delete_preserves_bst_property(self):
        """Test that BST property is preserved throughout deletions."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        
        for val in values:
            bst.insert(val)
        
        # Delete several nodes
        for val in [20, 40, 60, 80]:
            bst.delete_node(val)
        
        # Verify remaining values can be found
        remaining = [50, 30, 70, 10, 25, 35, 45, 55, 65, 75, 85]
        for val in remaining:
            assert bst.contains(val) is True


class TestBSTEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_single_node_tree(self):
        """Test operations on single node tree."""
        bst = BinarySearchTree()
        bst.insert(42)
        
        assert bst.contains(42) is True
        bst.delete_node(42)
        assert bst.root is None
    
    def test_left_skewed_tree(self):
        """Test deletion in left-skewed tree."""
        bst = BinarySearchTree()
        values = [10, 9, 8, 7, 6]
        for val in values:
            bst.insert(val)
        
        bst.delete_node(9)
        
        assert bst.contains(9) is False
        for val in [10, 8, 7, 6]:
            assert bst.contains(val) is True
    
    def test_right_skewed_tree(self):
        """Test deletion in right-skewed tree."""
        bst = BinarySearchTree()
        values = [1, 2, 3, 4, 5]
        for val in values:
            bst.insert(val)
        
        bst.delete_node(3)
        
        assert bst.contains(3) is False
        for val in [1, 2, 4, 5]:
            assert bst.contains(val) is True
    
    def test_delete_negative_values(self):
        """Test deletion with negative values."""
        bst = BinarySearchTree()
        values = [0, -5, 5, -10, -2, 2, 10]
        for val in values:
            bst.insert(val)
        
        bst.delete_node(-5)
        
        assert bst.contains(-5) is False
        for val in [0, 5, -10, -2, 2, 10]:
            assert bst.contains(val) is True
    
    def test_delete_with_duplicate_structure(self):
        """Test deletion when tree has similar subtree structures."""
        bst = BinarySearchTree()
        # Create balanced structure
        bst.insert(50)
        bst.insert(25)
        bst.insert(75)
        bst.insert(12)
        bst.insert(37)
        bst.insert(62)
        bst.insert(87)
        
        bst.delete_node(25)
        
        assert bst.contains(25) is False
        # Verify left and right subtrees are intact
        for val in [50, 75, 12, 37, 62, 87]:
            assert bst.contains(val) is True
