# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:        
        q=deque()
        q.append((root,None, None))
        level=0
        ans=[]
        while q:
            levelSize=len(q)
            for i in range(levelSize):
                curr, gp, p=q.popleft()                
                if level>1 and gp%2==0:
                    ans.append(curr.val)
                if curr.left:
                    q.append((curr.left, p, curr.val))
                if curr.right:
                    q.append((curr.right, p, curr.val))
            level+=1
        return sum(ans)
    
        # ans=[]
        # def helper(node, level, p):
        #     if not node:
        #         return 0
        #     if level>1 and p[0]%2==0:
        #         ans.append(node.val)
        #     helper(node.left,level+1, [p[-1], node.val])
        #     helper(node.right, level+1, [p[-1], node.val])
        # helper(root, 0, [None, None])
        # return sum(ans)
        
