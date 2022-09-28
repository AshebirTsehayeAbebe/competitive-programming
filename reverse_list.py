class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        previous, current = None, head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
