def removeNthFromEnd(head, n):
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head

    # Initialize the fast and slow pointers
    fast = dummy
    slow = dummy

    # Move the fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers until the fast pointer reaches the end
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Remove the nth node from the end
    slow.next = slow.next.next

    # Return the head of the modified linked list
    return dummy.next

