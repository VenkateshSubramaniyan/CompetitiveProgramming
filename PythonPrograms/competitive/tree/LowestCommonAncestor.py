# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# first we search for left and right, if match found we return value else null
# The point at which the both left and right is not null has  is the lowest common anchestor

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if  root is None or root.val is p or root.val is q:
            return root

        left =self.lowestCommonAncestor(root.left,p,q)
        right =self.lowestCommonAncestor(root.right,p,q)

        if not left:
            return  right

        if not right:
            return  left
        return root


head=  TreeNode(3);
head.left= TreeNode(5)
head.right= TreeNode(1)
head.left.left= TreeNode(6)
head.left.right= TreeNode(2)
head.right.left= TreeNode(0)
head.right.right= TreeNode(8)
head.left.right.left= TreeNode(7)
head.left.right.right= TreeNode(4)
print(Solution().lowestCommonAncestor(head,5,1).val)
print(Solution().lowestCommonAncestor(head,5,4).val)

