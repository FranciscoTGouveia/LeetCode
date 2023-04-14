class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        output = []
        def traverse(root):
            if root:
                traverse(root.left)
                output.append(root.val)
                traverse(root.right)
        traverse(root)
        return output
