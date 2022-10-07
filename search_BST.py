# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:     
        q = deque()
        q.append(root)
        while len(q) > 0:
            curr = q.popleft()
            if curr.val==val:
                return curr
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return None  
