# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q=deque()
        q.append(root)
        maxLen=0
        level=0
        tempList=[]
        while q:
            maxLen=len(q)
            if level>0 and maxLen%2!=0:
                return False
            for i in range(maxLen):
                temp=q.popleft()
                if temp:
                    q.append(temp.left)
                    q.append(temp.right)
                tempList.append(temp.val if temp else temp)
            if maxLen==1:
                tempList.pop()  
                level+=1
                continue
            for i in range(maxLen//2):
                temp1=tempList.pop(0)
                temp2=tempList.pop()                
                if temp1!=temp2:
                    return False            
            level+=1
        return True
