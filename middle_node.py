# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size=0
        temp=head
        while temp:
            temp=temp.next
            size+=1
        counter=0
        while head:
            counter+=1
            if counter==math.ceil((size+1)/2):
                return head
            head=head.next
            
