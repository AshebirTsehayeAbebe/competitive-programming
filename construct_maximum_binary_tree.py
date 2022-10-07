# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxNumber=max(nums)
        maxIndex=nums.index(maxNumber)
        maxNode = TreeNode(maxNumber)        
        
        if len(nums[:maxIndex]):
            maxNode.left=self.constructMaximumBinaryTree(nums[:maxIndex])
        if len(nums[maxIndex+1:]):
            maxNode.right=self.constructMaximumBinaryTree(nums[maxIndex+1:])
        return maxNode
            
        
