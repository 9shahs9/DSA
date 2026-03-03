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


class TestBSTMinValue:
    """Test cases for min_value function."""
    
    def test_min_value_none_node(self):
        """Test min_value with None node."""
        bst = BinarySearchTree()
        result = bst.min_value(None)
        
        assert result is None
    
    def test_min_value_single_node(self):
        """Test min_value with single node tree."""
        bst = BinarySearchTree()
        bst.insert(10)
        
        min_val = bst.min_value(bst.root)
        assert min_val == 10
    
    def test_min_value_left_skewed_tree(self):
        """Test min_value in left-skewed tree."""
        bst = BinarySearchTree()
        values = [10, 9, 8, 7, 6]
        for val in values:
            bst.insert(val)
        
        min_val = bst.min_value(bst.root)
        assert min_val == 6
    
    def test_min_value_right_skewed_tree(self):
        """Test min_value in right-skewed tree (min is root)."""
        bst = BinarySearchTree()
        values = [1, 2, 3, 4, 5]
        for val in values:
            bst.insert(val)
        
        min_val = bst.min_value(bst.root)
        assert min_val == 1
    
    def test_min_value_balanced_tree(self):
        """Test min_value in balanced tree."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            bst.insert(val)
        
        min_val = bst.min_value(bst.root)
        assert min_val == 20
    
    def test_min_value_right_subtree(self):
        """Test min_value on right subtree only."""
        bst = BinarySearchTree()
        values = [10, 5, 20, 15, 25]
        for val in values:
            bst.insert(val)
        
        # Get minimum of right subtree
        min_val = bst.min_value(bst.root.right)
        assert min_val == 15
    
    def test_min_value_left_subtree(self):
        """Test min_value on left subtree only."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            bst.insert(val)
        
        # Get minimum of left subtree
        min_val = bst.min_value(bst.root.left)
        assert min_val == 20
    
    def test_min_value_deep_left_path(self):
        """Test min_value with deep left path."""
        bst = BinarySearchTree()
        bst.insert(100)
        bst.insert(50)
        bst.insert(25)
        bst.insert(12)
        bst.insert(6)
        bst.insert(3)
        bst.insert(1)
        
        min_val = bst.min_value(bst.root)
        assert min_val == 1
    
    def test_min_value_with_right_child(self):
        """Test min_value when leftmost node has right child."""
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(30)
        bst.insert(70)
        bst.insert(20)
        bst.insert(10)
        bst.insert(15)  # Right child of leftmost node
        
        min_val = bst.min_value(bst.root)
        assert min_val == 10
    
    def test_min_value_negative_numbers(self):
        """Test min_value with negative numbers."""
        bst = BinarySearchTree()
        values = [0, -10, 10, -20, -5, 5, 15]
        for val in values:
            bst.insert(val)
        
        min_val = bst.min_value(bst.root)
        assert min_val == -20
    
    def test_min_value_all_negative(self):
        """Test min_value with all negative values."""
        bst = BinarySearchTree()
        values = [-5, -10, -3, -15, -8, -1]
        for val in values:
            bst.insert(val)
        
        min_val = bst.min_value(bst.root)
        assert min_val == -15
    
    def test_min_value_mixed_signs(self):
        """Test min_value with mixed positive and negative."""
        bst = BinarySearchTree()
        values = [10, -5, 20, -10, 0, 15, 25]
        for val in values:
            bst.insert(val)
        
        min_val = bst.min_value(bst.root)
        assert min_val == -10
    
    def test_min_value_large_values(self):
        """Test min_value with large numbers."""
        bst = BinarySearchTree()
        values = [1000000, 500000, 1500000, 250000, 125000]
        for val in values:
            bst.insert(val)
        
        min_val = bst.min_value(bst.root)
        assert min_val == 125000
    
    def test_min_value_different_subtrees(self):
        """Test min_value on different subtrees of same tree."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for val in values:
            bst.insert(val)
        
        # Min of entire tree
        assert bst.min_value(bst.root) == 10
        
        # Min of left subtree
        assert bst.min_value(bst.root.left) == 10
        
        # Min of right subtree
        assert bst.min_value(bst.root.right) == 55
    
    def test_min_value_after_deletion(self):
        """Test min_value after deleting minimum element."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 10]
        for val in values:
            bst.insert(val)
        
        # Min before deletion
        assert bst.min_value(bst.root) == 10
        
        # Delete minimum
        bst.delete_node(10)
        
        # Min after deletion
        assert bst.min_value(bst.root) == 20
    
    def test_min_value_empty_tree_root_comparison(self):
        """Test min_value on empty tree vs non-empty root."""
        bst = BinarySearchTree()
        bst.insert(50)
        
        # Empty node returns None
        assert bst.min_value(None) is None
        
        # Root exists
        assert bst.min_value(bst.root) == 50
    
    def test_min_value_single_left_child(self):
        """Test min_value when only left child exists."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        
        min_val = bst.min_value(bst.root)
        assert min_val == 5
    
    def test_min_value_single_right_child(self):
        """Test min_value when only right child exists."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(15)
        
        min_val = bst.min_value(bst.root)
        assert min_val == 10


class TestMinValueIntegration:
    """Integration tests for min_value function."""
    
    def test_min_value_used_in_delete(self):
        """Test min_value function as used in delete_node."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            bst.insert(val)
        
        # Delete node with two children - uses min_value internally
        bst.delete_node(50)
        
        # Root should be replaced with min of right subtree (60)
        assert bst.root.value == 60
        assert bst.contains(50) is False
    
    def test_min_value_sequence(self):
        """Test min_value in sequence of operations."""
        bst = BinarySearchTree()
        
        # Insert and check min
        bst.insert(100)
        assert bst.min_value(bst.root) == 100
        
        bst.insert(50)
        assert bst.min_value(bst.root) == 50
        
        bst.insert(200)
        assert bst.min_value(bst.root) == 50
        
        bst.insert(25)
        assert bst.min_value(bst.root) == 25
        
        bst.insert(10)
        assert bst.min_value(bst.root) == 10
    
    def test_min_value_preserves_tree(self):
        """Test that min_value doesn't modify the tree."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            bst.insert(val)
        
        # Call min_value multiple times
        for _ in range(5):
            min_val = bst.min_value(bst.root)
        
        # Tree should remain intact
        assert min_val == 20
        for val in values:
            assert bst.contains(val) is True
    
    def test_min_value_duplicate_values_at_left(self):
        """Test min_value behavior doesn't change after operations."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 10, 15]
        for val in values:
            bst.insert(val)
        
        # Min should remain consistent
        for _ in range(3):
            assert bst.min_value(bst.root) == 10
            assert bst.min_value(bst.root.left) == 10
            assert bst.min_value(bst.root.right) == 70
