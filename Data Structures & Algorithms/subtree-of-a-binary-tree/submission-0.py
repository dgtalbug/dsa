# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # Check if the trees match at the current node or any subtree
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Both trees are None, so they are the same
        if not root and not subRoot:
            return True
        
        # One tree is None, or the values are different
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        # Recursively check left and right subtrees
        return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
