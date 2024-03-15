#Given the head of a linked list, remove the nth node from the end of the list and return its head.
from tkinter.tix import ListNoteBook


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

# Time complexity: O(n)
# Space complexity: O(1)
# The algorithm makes one traversal of the list of n nodes. Therefore, the time complexity is O(n).