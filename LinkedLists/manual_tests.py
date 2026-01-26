import pytest
import sys
import os

# Add the LinkedLists directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from intro import LinkedList


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(5)


ll.leet_code_remove_duplicates()
ll.print_list()

ll2 = LinkedList(1)
ll2.append(2)
ll2.append(3)
ll2.append(1)
ll2.append(4)
ll2.append(2)
ll2.append(5)

ll2.leet_code_remove_duplicate_nested()
ll2.print_list()


l3 = LinkedList(1)
l3.append(0)
l3.append(0)
l3.append(0)

print(l3.leet_code_binary_to_decimal())

"""
3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5
"""

l4 = LinkedList(3)
l4.append(8)
l4.append(5)
l4.append(10)
l4.append(2)
l4.append(1)

l4.leet_code_partition_list_dummy_nodes(5) 
l4.print_list()

l4.leet_code_reverse_between(1,5)
l4.print_list()


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.leet_code_reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.leet_code_reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.leet_code_reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.leet_code_reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()