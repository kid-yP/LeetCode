# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        x = y = None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                y = nodes[i + 1]
                if not x:
                    x = nodes[i]
                else:
                    break

        x.val, y.val = y.val, x.val    