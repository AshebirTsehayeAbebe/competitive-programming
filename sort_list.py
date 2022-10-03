# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        list=[]
        temp=head
        while head: 
            list.append(head.val)
            head=head.next
        list.sort()
        newNode=ListNode(list[0])
        p=newNode
        for i in range(1,len(list)):
            node=ListNode(list[i])
            p.next=node
            p=node
            temp=temp.next
        return newNode
            
