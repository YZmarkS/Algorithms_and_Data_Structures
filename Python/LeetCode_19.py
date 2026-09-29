class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        front = head
        for _ in range(n):
            front = front.next

        if front is None:
            return head.next

        behind_back = ListNode(0, head)
        back = head

        while front is not None:
            front = front.next
            back = back.next
            behind_back = behind_back.next

        behind_back.next = back.next

        return head
