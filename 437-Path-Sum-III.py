# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        lookup = {0: 1}
        
        def dfs(node, currentPathSum, lookup):
            if node is None:
                return

            currentPathSum += node.val
            oldPathSum = currentPathSum - targetSum

            self.paths += lookup.get(oldPathSum, 0)
            lookup[currentPathSum] = lookup.get(currentPathSum, 0) + 1

            dfs(node.left, currentPathSum, lookup)
            dfs(node.right, currentPathSum, lookup)
            
            lookup[currentPathSum] -= 1
        
        dfs(root, 0, lookup)
        return self.paths