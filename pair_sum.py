# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum=0
        prev, curr =None, head
        list=[]
        while curr:
            list.append(curr.val)
            nextNode=curr.next
            curr.next=prev
            prev = curr            
            curr=nextNode
        counter=0
        while prev:
            maxSum=max(maxSum, prev.val+list[counter])
            counter+=1
            prev=prev.next
        return maxSum
