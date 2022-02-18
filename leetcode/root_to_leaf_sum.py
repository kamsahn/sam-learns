# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        if targetSum == root.val and not root.left and not root.right:
            return True

        leftOutcome = rightOutcome = None
        if root.left:
            leftOutcome = self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            rightOutcome = self.hasPathSum(root.right, targetSum - root.val)

        if leftOutcome or rightOutcome:
            return True

        return False