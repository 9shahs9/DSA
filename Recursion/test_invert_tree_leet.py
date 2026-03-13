import unittest
from invert_tree_leet import BinarySearchTree, Node


class TestInvertTree(unittest.TestCase):
    """Test cases for inverting a binary search tree."""
    
    def setUp(self):
        """Initialize a fresh BinarySearchTree for each test."""
        self.bst = BinarySearchTree()
    
    def _tree_to_level_order(self, node):
        """Convert tree to level-order list representation."""
        if not node:
            return []
        queue = [node]
        result = []
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.value)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        # Clean up trailing None values
        while result and result[-1] is None:
            result.pop()
        return result
    
    def _verify_inversion(self, original_list, inverted_list):
        """Verify that a list is the inverted version of another."""
        if not original_list and not inverted_list:
            return True
        if len(original_list) != len(inverted_list):
            return False
        # Build original tree
        bst_original = BinarySearchTree()
        for val in original_list:
            bst_original.r_insert(val)
        original = self._tree_to_level_order(bst_original.root)
        
        # Build inverted tree
        bst_inverted = BinarySearchTree()
        for val in inverted_list:
            bst_inverted.r_insert(val)
        inverted = self._tree_to_level_order(bst_inverted.root)
        
        return original == inverted
    
    def test_empty_tree(self):
        """Test inverting an empty tree."""
        self.bst.invert()
        self.assertIsNone(self.bst.root)
        self.assertEqual(self._tree_to_level_order(self.bst.root), [])
    
    def test_single_node(self):
        """Test inverting a tree with a single node."""
        self.bst.r_insert(5)
        self.bst.invert()
        self.assertEqual(self.bst.root.value, 5)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)
        self.assertEqual(self._tree_to_level_order(self.bst.root), [5])
    
    def test_two_nodes_left_child(self):
        """Test inverting a tree with a root and left child."""
        self.bst.r_insert(2)
        self.bst.r_insert(1)
        self.bst.invert()
        # After inversion, left becomes right
        self.assertEqual(self.bst.root.value, 2)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNotNone(self.bst.root.right)
        self.assertEqual(self.bst.root.right.value, 1)
    
    def test_two_nodes_right_child(self):
        """Test inverting a tree with a root and right child."""
        self.bst.r_insert(1)
        self.bst.r_insert(2)
        self.bst.invert()
        # After inversion, right becomes left
        self.assertEqual(self.bst.root.value, 1)
        self.assertIsNotNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)
        self.assertEqual(self.bst.root.left.value, 2)
    
    def test_three_nodes_balanced(self):
        """Test inverting a balanced tree with three nodes."""
        self.bst.r_insert(2)
        self.bst.r_insert(1)
        self.bst.r_insert(3)
        before = self._tree_to_level_order(self.bst.root)
        self.bst.invert()
        after = self._tree_to_level_order(self.bst.root)
        # Root stays the same
        self.assertEqual(after[0], 2)
        # Left and right swap at each level
        self.assertIsNotNone(self.bst.root.left)
        self.assertIsNotNone(self.bst.root.right)
        self.assertEqual(self.bst.root.left.value, 3)
        self.assertEqual(self.bst.root.right.value, 1)
    
    def test_multi_level_tree(self):
        """Test inverting a multi-level tree."""
        values = [4, 2, 6, 1, 3, 5, 7]
        for val in values:
            self.bst.r_insert(val)
        
        # Get tree structure before inversion
        before_level_order = self._tree_to_level_order(self.bst.root)
        
        # Invert the tree
        self.bst.invert()
        
        # After inversion, structure should be completely flipped
        # Left subtree becomes right and vice versa
        self.assertEqual(self.bst.root.value, 4)
        self.assertIsNotNone(self.bst.root.left)
        self.assertIsNotNone(self.bst.root.right)
        # After inversion, the original right subtree values should be on the left
        self.assertEqual(self.bst.root.left.value, 6)
        self.assertEqual(self.bst.root.right.value, 2)
    
    def test_double_inversion(self):
        """Test that inverting twice returns to original structure."""
        values = [4, 2, 6, 1, 3, 5, 7]
        for val in values:
            self.bst.r_insert(val)
        
        before = self._tree_to_inorder(self.bst.root)
        
        # Invert twice
        self.bst.invert()
        self.bst.invert()
        
        after = self._tree_to_inorder(self.bst.root)
        
        # Inorder traversal should be the same (all values preserved)
        self.assertEqual(before, after)
    
    def test_left_skewed_tree(self):
        """Test inverting a left-skewed tree."""
        self.bst.r_insert(5)
        self.bst.r_insert(4)
        self.bst.r_insert(3)
        self.bst.r_insert(2)
        self.bst.r_insert(1)
        
        self.bst.invert()
        
        # After inversion, left-skewed becomes right-skewed
        current = self.bst.root
        while current:
            self.assertIsNone(current.left)
            current = current.right
    
    def test_right_skewed_tree(self):
        """Test inverting a right-skewed tree."""
        self.bst.r_insert(1)
        self.bst.r_insert(2)
        self.bst.r_insert(3)
        self.bst.r_insert(4)
        self.bst.r_insert(5)
        
        self.bst.invert()
        
        # After inversion, right-skewed becomes left-skewed
        current = self.bst.root
        while current:
            self.assertIsNone(current.right)
            current = current.left
    
    def test_inversion_preserves_values(self):
        """Test that inversion preserves all values in the tree."""
        values = [4, 2, 6, 1, 3, 5, 7, 8]
        for val in values:
            self.bst.r_insert(val)
        
        values_before = self._get_all_values(self.bst.root)
        self.bst.invert()
        values_after = self._get_all_values(self.bst.root)
        
        self.assertEqual(sorted(values_before), sorted(values_after))
    
    def test_negative_numbers(self):
        """Test inverting a tree with negative numbers."""
        values = [0, -5, 5, -7, -3, 3, 7]
        for val in values:
            self.bst.r_insert(val)
        
        self.bst.invert()
        
        # Root should still be 0
        self.assertEqual(self.bst.root.value, 0)
        # Verify structure is inverted (left and right swapped)
        self.assertIsNotNone(self.bst.root.left)
        self.assertIsNotNone(self.bst.root.right)
        self.assertEqual(self.bst.root.left.value, 5)
        self.assertEqual(self.bst.root.right.value, -5)
    
    def test_large_tree(self):
        """Test inverting a large tree."""
        values = list(range(1, 32))  # 31 nodes
        for val in values:
            self.bst.r_insert(val)
        
        values_before = self._get_all_values(self.bst.root)
        self.bst.invert()
        values_after = self._get_all_values(self.bst.root)
        
        # All values should still be present
        self.assertEqual(sorted(values_before), sorted(values_after))
        # Root should still be 1 (first value inserted)
        self.assertEqual(self.bst.root.value, 1)
    
    def test_depth_structure_inversion(self):
        """Test that depth structure is properly inverted."""
        # Build specific structure
        self.bst.r_insert(10)
        self.bst.r_insert(5)
        self.bst.r_insert(15)
        self.bst.r_insert(3)
        self.bst.r_insert(7)
        
        # Before inversion
        self.assertEqual(self.bst.root.left.value, 5)
        self.assertEqual(self.bst.root.right.value, 15)
        self.assertEqual(self.bst.root.left.left.value, 3)
        self.assertEqual(self.bst.root.left.right.value, 7)
        
        self.bst.invert()
        
        # After inversion
        self.assertEqual(self.bst.root.left.value, 15)
        self.assertEqual(self.bst.root.right.value, 5)
        self.assertEqual(self.bst.root.right.left.value, 7)
        self.assertEqual(self.bst.root.right.right.value, 3)
    
    # Helper methods
    def _tree_to_inorder(self, node):
        """Convert tree to inorder traversal list."""
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node, result):
        """Helper for inorder traversal."""
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
    
    def _get_all_values(self, node):
        """Get all values in the tree (inorder)."""
        return self._tree_to_inorder(node)


if __name__ == '__main__':
    unittest.main()
