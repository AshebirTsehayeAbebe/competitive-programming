# Definition for singly-linked list.
class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode(0, head)
        prev, curr = newNode, head
        while curr and curr.next:
            nextPair=curr.next.next
            second=curr.next
            second.next=curr
            curr.next=nextPair
            prev.next=second
            prev=curr
            curr=nextPair
            
        return head
