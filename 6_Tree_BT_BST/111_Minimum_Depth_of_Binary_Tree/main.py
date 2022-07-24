# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        que = deque([])
        return search(root, 1, que)

def search(node: TreeNode, depth: int, que):
    if node.right is None and node.left is None:
        return depth 
    if node.left is not None:
        que.append((node.left, depth + 1))
    if node.right is not None:
        que.append((node.right, depth + 1))

    node_to_depth = que.popleft()
    return search(node_to_depth[0], node_to_depth[1], que)   