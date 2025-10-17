# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build_trees(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees

            for i in range(start, end + 1):
                left_subtrees = build_trees(start, i - 1)
                right_subtrees = build_trees(i + 1, end)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build_trees(1, n)