# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global result
        result = 0
        def dfs(root, greatest=None):
            global result
            if greatest == None:
                greatest = root.val
            if root.val >= greatest:
                result += 1
                greatest = max(greatest, root.val)
            if root.left:
                dfs(root.left, greatest)
            if root.right:
                dfs(root.right, greatest)
        dfs(root)
        return result