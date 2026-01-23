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
