# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        ans=[]
        flag=0
        if root:
            q.append(root)
        while q:
            levelSize=len(q)
            temp=[]
            for i in range(levelSize):
                curr=q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if flag==1:
                temp=temp[::-1]
            ans.append(temp)
            flag=not flag
        return ans
                
