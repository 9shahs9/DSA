"""
LL: Find Middle Node ( ** Interview Question)
Implement the find_middle_node method for the LinkedList class.

Note: this LinkedList implementation does not have a length member variable.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once.  In other words, you can only use one loop.
"""

def find_middle_node (ll):
    fast = ll.head
    slow = ll.head
    while fast!= None and fast!=ll.tail:
        slow = slow.next
        if fast.next == None or fast.next.next == None:
            break 
        fast = fast.next.next
    return slow 



"""
LL: Has Loop ( ** Interview Question)
Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.

This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

The method should follow these guidelines:
"""

def has_loop(ll):
    fast = ll.head 
    slow = ll.head
    while (fast != None):
        slow = slow.next
        if (fast.next == None or fast.next.next == None):
            return False 
        fast = fast.next.next
        if fast == slow:
            return True 
    return False 


"""
LL: Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.



NOTE: This is a SEPARATE FUNCTION that is NOT a method within the LinkedList class.  This means you need to indent the function all the way to the LEFT. 



Given this LinkedList:

1 -> 2 -> 3 -> 4 -> 5

If k=1 then return the first node from the end (the last node) which contains the value of 5.

If k=2 then return the second node from the end which contains the value of 4, etc.

If the index is out of bounds, the program should return None.

The find_kth_from_end function should follow these requirements:

The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

The fast pointer should move k nodes ahead in the list.

If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

The function should return the slow pointer, which will be at the k-th position from the end of the list.
"""

def find_kth_from_end(ll, k):       
    fast = ll.head
    slow = ll.head 
    for _ in range(k-1):
        if fast == ll.tail:
            return None 
        if fast.next :
            fast = fast.next 
    while fast != ll.tail:
        fast = fast.next 
        slow = slow.next
    return slow 


"""
LL: Remove Duplicates ( ** Interview Question)
You are given a singly linked list that contains integer values, where some of these values may be duplicated.

Note: this linked list class does NOT have a tail which will make this method easier to implement.

Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

You can implement the remove_duplicates() method in two different ways:



Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.



Here is the method signature you need to implement:

def remove_duplicates(self):


Example:

Input:

LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5

Output:

LinkedList: 1 -> 2 -> 3 -> 4 -> 5


"""


def remove_duplicates(ll):
        seen = set()
        prev = ll.head 
        curr = ll.head 
        while(curr != None):
            if curr.value in seen:
                prev.next = curr.next 
            else:
                seen.add(curr.value)
                prev = curr
            curr = curr.next


def remove_duplicate_nested(ll):
    curr = ll.head 
    runner = ll.head 
    while curr!=None :
        while runner.next != None:
            if curr.value == runner.next.value:
                runner.next = runner.next.next 
            runner = runner.next 
        if curr.next == None:
            break 
        curr = curr.next 
        runner = curr


def binary_to_decimal(ll):
        length = 0 
        curr = ll.head 
        while curr!=None:
            length +=1 
            curr = curr.next 
        
        value = 0 
        curr = ll.head 
        while curr!=None:
            value += (2**(length-1))*curr.value 
            length -=1 
            curr = curr.next 
        return value 





def partition_list(ll, x):   
    left_init = 0
    right_init = 0
    curr = ll.head
    if curr == None:
        return 
    while(curr != None):
        if curr.value < x:
            if left_init == 0:
                left = LinkedList(curr.value)
                left_init = 1 
            else: 
                left.append(curr.value)
        else:
            if right_init == 0:
                right = LinkedList(curr.value)
                right_init = 1 
            else:
                right.append(curr.value)
        curr = curr.next 
    
    ll.make_empty()
    if left_init == 0:
        ll = right 
        return 
    
    ll = left 
    if right_init == 0:
        return 
    curr = ll.head 
    while(curr.next != None):
        curr = curr.next 
    curr.next = right.head 


