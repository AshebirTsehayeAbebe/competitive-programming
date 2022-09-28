# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list=[]
        while head:
            list.append(head.val)
            head=head.next
        list.sort()
        for i in range(1, len(list)):
            j=i-1
            key=list[i]
            while j>=0 and key<list[i]:
                list[j+1]=list[j]
                j-=1
            list[j+1]=key
        newHead=ListNode(0)
        for i in range(len(list)-1,-1,-1):
            if i==len(list)-1:
                newHead.val=list[i]
            else:
                newNode=ListNode(list[i])
                newNode.next=newHead
                newHead=newNode
        return newHead
            
