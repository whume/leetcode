"""
Question 101:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Technically a empty tree could be symmetric
        if root == None:
            return True
        # Return recursive loop to keep logic clean
        return self.isMirror(root, root)

    def isMirror(self, left, right):
        # left and Right matching is symmetric so we can stop and return True
        if left is None and right is None:
            return True
        # If Left or Right is empty but not both they don't match so we return False
        elif left is None or right is None:
            return False
            # Finally we return the comparison of the values and we recurse through the children nodes. If all matches we returnb True
        else:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
