# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p ,q)
        if left != None and right != None:
            return root
        elif left != None:
            return left
        elif right != None:
            return right
        else:
            return None

#其他高级解法请参考：https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/03.03.md
