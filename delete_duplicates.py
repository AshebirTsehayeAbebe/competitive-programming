class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if temp is None:
            return
        while temp.next is not None:
            if temp.val == temp.next.val:
                new = temp.next.next
                temp.next = new
            else:
                temp = temp.next
        return head
