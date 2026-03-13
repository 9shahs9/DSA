import unittest
from leet_balanced_btree import BinarySearchTree, Node


class TestSortedListToBST(unittest.TestCase):
    """Test cases for converting a sorted list to a balanced binary search tree."""
    
    def setUp(self):
        """Initialize a fresh BinarySearchTree for each test."""
        self.bst = BinarySearchTree()
    
    def test_empty_list(self):
        """Test converting an empty list should result in an empty tree."""
        self.bst.sorted_list_to_bst([])
        self.assertIsNone(self.bst.root)
        self.assertEqual(self.bst.inorder_traversal(), [])
        self.assertTrue(self.bst.is_balanced())
    
    def test_single_element(self):
        """Test converting a list with one element."""
        self.bst.sorted_list_to_bst([5])
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.value, 5)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)
        self.assertEqual(self.bst.inorder_traversal(), [5])
        self.assertTrue(self.bst.is_balanced())
    
    def test_two_elements(self):
        """Test converting a list with two elements."""
        self.bst.sorted_list_to_bst([1, 2])
        self.assertEqual(self.bst.inorder_traversal(), [1, 2])
        self.assertTrue(self.bst.is_balanced())
    
    def test_odd_number_of_elements(self):
        """Test converting a sorted list with odd number of elements."""
        self.bst.sorted_list_to_bst([1, 2, 3, 4, 5])
        self.assertEqual(self.bst.inorder_traversal(), [1, 2, 3, 4, 5])
        self.assertTrue(self.bst.is_balanced())
        # Root should be 3 (middle element)
        self.assertEqual(self.bst.root.value, 3)
    
    def test_even_number_of_elements(self):
        """Test converting a sorted list with even number of elements."""
        self.bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
        self.assertEqual(self.bst.inorder_traversal(), [1, 2, 3, 4, 5, 6])
        self.assertTrue(self.bst.is_balanced())
    
    def test_large_sorted_list(self):
        """Test converting a large sorted list."""
        large_list = list(range(1, 16))  # 1 to 15
        self.bst.sorted_list_to_bst(large_list)
        self.assertEqual(self.bst.inorder_traversal(), large_list)
        self.assertTrue(self.bst.is_balanced())
    
    def test_negative_numbers(self):
        """Test converting a sorted list with negative numbers."""
        self.bst.sorted_list_to_bst([-5, -3, -1, 0, 2, 4])
        self.assertEqual(self.bst.inorder_traversal(), [-5, -3, -1, 0, 2, 4])
        self.assertTrue(self.bst.is_balanced())
    
    def test_mixed_positive_negative_numbers(self):
        """Test converting a sorted list with mixed positive and negative numbers."""
        self.bst.sorted_list_to_bst([-10, -5, 0, 5, 10])
        self.assertEqual(self.bst.inorder_traversal(), [-10, -5, 0, 5, 10])
        self.assertTrue(self.bst.is_balanced())
    
    def test_duplicates(self):
        """Test converting a sorted list with duplicate elements."""
        self.bst.sorted_list_to_bst([1, 2, 2, 3, 3, 3])
        self.assertEqual(self.bst.inorder_traversal(), [1, 2, 2, 3, 3, 3])
        self.assertTrue(self.bst.is_balanced())
    
    def test_bst_property(self):
        """Test that the resulting tree maintains BST property."""
        self.bst.sorted_list_to_bst([1, 2, 3, 4, 5])
        self._verify_bst_property(self.bst.root)
    
    def test_tree_height_difference(self):
        """Test that the height difference between subtrees is at most 1."""
        self.bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6, 7])
        max_height_diff = self._get_max_height_diff(self.bst.root)
        self.assertLessEqual(max_height_diff, 1)
    
    def test_large_range(self):
        """Test converting a large range of numbers."""
        large_list = list(range(0, 100))
        self.bst.sorted_list_to_bst(large_list)
        self.assertEqual(self.bst.inorder_traversal(), large_list)
        self.assertTrue(self.bst.is_balanced())
    
    def test_root_middle_element(self):
        """Test that root is approximately the middle element."""
        self.bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6, 7, 8, 9])
        # For odd length, root should be the exact middle
        # Middle index for length 9 is 4, value is 5
        self.assertEqual(self.bst.root.value, 5)
    
    def test_three_elements(self):
        """Test converting a list with three elements."""
        self.bst.sorted_list_to_bst([10, 20, 30])
        self.assertEqual(self.bst.root.value, 20)
        self.assertEqual(self.bst.root.left.value, 10)
        self.assertEqual(self.bst.root.right.value, 30)
        self.assertEqual(self.bst.inorder_traversal(), [10, 20, 30])
        self.assertTrue(self.bst.is_balanced())
    
    # Helper methods
    def _verify_bst_property(self, node, min_val=float('-inf'), max_val=float('inf')):
        """
        Verify that the tree maintains BST property:
        - All left values < node value
        - All right values > node value
        """
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self._verify_bst_property(node.left, min_val, node.value) and
                self._verify_bst_property(node.right, node.value, max_val))
    
    def _get_max_height_diff(self, node):
        """Get the maximum height difference in the tree."""
        if node is None:
            return 0
        
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        height_diff = abs(left_height - right_height)
        
        left_max_diff = self._get_max_height_diff(node.left)
        right_max_diff = self._get_max_height_diff(node.right)
        
        return max(height_diff, left_max_diff, right_max_diff)
    
    def _get_height(self, node):
        """Get the height of a node in the tree."""
        if node is None:
            return -1
        return 1 + max(self._get_height(node.left), self._get_height(node.right))


if __name__ == '__main__':
    unittest.main()
