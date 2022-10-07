# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        left_max = root.val
        while len(queue) > 0:
            level_size = len(queue)
            for i in range(level_size):
                temp = queue.pop(0)
                if i == 0:
                    left_max = temp.val
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return left_max
