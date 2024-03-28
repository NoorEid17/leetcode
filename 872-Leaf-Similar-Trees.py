# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafs(root, res):
            if root.left == None and root.right == None:
                res.append(root.val)
            if root.left:
                leafs(root.left, res)
            if root.right:
                leafs(root.right, res)
            return res
        leafs1 = []
        leafs2 = []
        leafs(root1, leafs1)
        leafs(root2, leafs2)
        return leafs1 == leafs2