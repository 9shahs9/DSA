import pytest
from io import StringIO
import sys
from main import Node, BinarySearchTree


class TestNode:
    """Test cases for Node class."""
    
    def test_node_init(self):
        """Test node initialization."""
        node = Node(5)
        assert node.value == 5
        assert node.left is None
        assert node.right is None
    
    def test_node_init_different_values(self):
        """Test node with different value types."""
        node1 = Node(10)
        assert node1.value == 10
        
        node2 = Node(-5)
        assert node2.value == -5
        
        node3 = Node(0)
        assert node3.value == 0


class TestBinarySearchTree:
    """Test cases for BinarySearchTree class."""
    
    def test_bst_init(self):
        """Test BST initialization."""
        bst = BinarySearchTree()
        assert bst.root is None
    
    def test_is_empty_on_new_tree(self):
        """Test is_empty on newly created tree."""
        bst = BinarySearchTree()
        assert bst.is_empty() is True
    
    def test_is_empty_after_insert(self):
        """Test is_empty after inserting a node."""
        bst = BinarySearchTree()
        bst.insert(10)
        assert bst.is_empty() is False
    
    def test_insert_single_value(self):
        """Test inserting a single value."""
        bst = BinarySearchTree()
        bst.insert(10)
        assert bst.root is not None
        assert bst.root.value == 10
        assert bst.root.left is None
        assert bst.root.right is None
    
    def test_insert_multiple_values_left_and_right(self):
        """Test inserting multiple values."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        
        assert bst.root.value == 10
        assert bst.root.left.value == 5
        assert bst.root.right.value == 15
    
    def test_insert_creates_bst_structure(self):
        """Test that insertions maintain BST property."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            bst.insert(v)
        
        # Check root
        assert bst.root.value == 50
        
        # Check left subtree
        assert bst.root.left.value == 30
        assert bst.root.left.left.value == 20
        assert bst.root.left.right.value == 40
        
        # Check right subtree
        assert bst.root.right.value == 70
        assert bst.root.right.left.value == 60
        assert bst.root.right.right.value == 80
    
    def test_insert_duplicate_values(self):
        """Test inserting duplicate values."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(10)
        
        # Duplicates should go right
        assert bst.root.value == 10
        assert bst.root.right.value == 10
    
    def test_insert_chain_left(self):
        """Test inserting values in descending order."""
        bst = BinarySearchTree()
        values = [50, 40, 30, 20, 10]
        for v in values:
            bst.insert(v)
        
        # Should create a chain on the left
        curr = bst.root
        for expected_val in values:
            assert curr.value == expected_val
            if expected_val != 10:
                curr = curr.left
    
    def test_insert_chain_right(self):
        """Test inserting values in ascending order."""
        bst = BinarySearchTree()
        values = [10, 20, 30, 40, 50]
        for v in values:
            bst.insert(v)
        
        # Should create a chain on the right
        curr = bst.root
        for expected_val in values:
            assert curr.value == expected_val
            if expected_val != 50:
                curr = curr.right
    
    def test_display_empty_tree(self, capsys):
        """Test display on empty tree."""
        bst = BinarySearchTree()
        bst.display()
        captured = capsys.readouterr()
        assert "Tree is empty" in captured.out
    
    def test_display_single_node(self, capsys):
        """Test display with single node."""
        bst = BinarySearchTree()
        bst.insert(10)
        bst.display()
        captured = capsys.readouterr()
        assert "10" in captured.out
    
    def test_display_multiple_nodes(self, capsys):
        """Test display with multiple nodes."""
        bst = BinarySearchTree()
        values = [10, 5, 15]
        for v in values:
            bst.insert(v)
        bst.display()
        captured = capsys.readouterr()
        
        # All values should be in output
        for v in values:
            assert str(v) in captured.out
        
        # Should contain tree structure characters
        assert "├──" in captured.out or "└──" in captured.out
    
    def test_display_complex_tree(self, capsys):
        """Test display with more complex tree structure."""
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            bst.insert(v)
        bst.display()
        captured = capsys.readouterr()
        
        # All values should appear
        for v in values:
            assert str(v) in captured.out
    
    def test_bst_property_maintained(self):
        """Test that BST property is maintained."""
        bst = BinarySearchTree()
        values = [47, 21, 76, 18, 52, 82, 27]
        for v in values:
            bst.insert(v)
        
        # Verify BST property: left < parent < right
        def verify_bst(node, min_val=float('-inf'), max_val=float('inf')):
            if node is None:
                return True
            
            if node.value <= min_val or node.value >= max_val:
                return False
            
            return (verify_bst(node.left, min_val, node.value) and 
                    verify_bst(node.right, node.value, max_val))
        
        assert verify_bst(bst.root) is True
    
    def test_insert_negative_values(self):
        """Test inserting negative values."""
        bst = BinarySearchTree()
        bst.insert(0)
        bst.insert(-10)
        bst.insert(10)
        
        assert bst.root.value == 0
        assert bst.root.left.value == -10
        assert bst.root.right.value == 10
    
    def test_insert_large_values(self):
        """Test inserting large values."""
        bst = BinarySearchTree()
        large_val = 1000000
        bst.insert(large_val)
        assert bst.root.value == large_val
    
    def test_multiple_insertions_maintains_structure(self):
        """Test that multiple insertions maintain the BST structure."""
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()
        
        values = [50, 25, 75, 12, 37, 62, 87]
        
        # Insert in same order
        for v in values:
            bst1.insert(v)
        
        # Insert in different order - should have same structure when traversed
        for v in reversed(values):
            bst2.insert(v)
        
        # Both should have the same values at the same positions eventually
        # (though structure might differ, both should be valid BSTs)
        def get_inorder(node, result=None):
            if result is None:
                result = []
            if node is None:
                return result
            get_inorder(node.left, result)
            result.append(node.value)
            get_inorder(node.right, result)
            return result
        
        assert get_inorder(bst1.root) == sorted(values)
        assert get_inorder(bst2.root) == sorted(values)


class TestBinarySearchTreeEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_insert_zero(self):
        """Test inserting zero."""
        bst = BinarySearchTree()
        bst.insert(0)
        assert bst.root.value == 0
    
    def test_display_doesnt_crash_on_complex_tree(self, capsys):
        """Ensure display doesn't crash on any valid tree."""
        bst = BinarySearchTree()
        values = list(range(1, 16))
        for v in values:
            bst.insert(v)
        
        # Should not raise any exception
        bst.display()
        captured = capsys.readouterr()
        assert captured.out is not None
