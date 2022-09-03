class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0, head)
        pred = sentinel
        print(pred)
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next 
            else:
                pred = pred.next
            head = head.next
        print(sentinel.next)   
        return sentinel.next
