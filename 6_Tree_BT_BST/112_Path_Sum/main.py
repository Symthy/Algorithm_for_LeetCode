# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        has_sum_left = False
        has_sum_right = False
        if root.left is not None:
            has_sum_left = self.search(root.left, root.val, targetSum)
        if root.right is not None:
            has_sum_right = self.search(root.right, root.val, targetSum)
        return has_sum_left or has_sum_right

    def search(self, node: Optional[TreeNode], sum_value, targetSum: int) -> bool:
        if node.right is None and node.left is None:
            return sum_value + node.val == targetSum

        has_sum_left = False
        has_sum_right = False
        updated_sum_value = sum_value + node.val
        if node.left is not None:
            has_sum_left = self.search(node.left, updated_sum_value, targetSum)
        if node.right is not None:
            has_sum_right = self.search(node.right, updated_sum_value, targetSum)
        return has_sum_left or has_sum_right
