# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        paths = []
        def dfs(root, sum=0, path=[]):
            newPath = path + [root.val]
            sum += root.val
            if sum == targetSum and root.left == root.right == None:
                paths.append(newPath)
                return
            else:
                if root.left:
                    dfs(root.left, sum, newPath)
                if root.right:
                    dfs(root.right, sum, newPath)
        dfs(root)
        return paths