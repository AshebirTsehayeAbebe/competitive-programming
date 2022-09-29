class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
            
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
            if prev.val!=list[counter]:
                return False
            counter+=1
            prev=prev.next
        return True
