# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        def dfs(root, sum=0):
            result = False
            sum += root.val
            if sum == targetSum and root.left == None and root.right == None:
                result = True
            else:
                if root.left:
                    result = dfs(root.left, sum) or result
                if root.right:
                    result = dfs(root.right, sum) or result
            return result
        return dfs(root)