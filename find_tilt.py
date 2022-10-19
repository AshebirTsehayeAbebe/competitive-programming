# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root:
                return 0,0
            leftVal, leftSum=helper(root.left)
            rigthVal, rightSum=helper(root.right)
            returnValue=leftVal+rigthVal+root.val
            root.val=abs(leftVal-rigthVal)
            return returnValue, leftSum+rightSum+root.val
        
        rv, sum=helper(root)
        return sum
