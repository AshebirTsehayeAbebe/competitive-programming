import collections
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans=[]
        
        def helper(node, level, p):
            if not node:
                return 0
            if level>1 and p[0]%2==0:
                ans.append(node.val)
            helper(node.left,level+1, [p[-1], node.val])
            helper(node.right, level+1, [p[-1], node.val])
        helper(root, 0, [None, None])
        return sum(ans)
