def isSymmetric(root: TreeNode) -> bool:
    if not root or (not root.left and not root.right):
        return True

    if not root.left or not root.right or root.left.val != root.right.val:
        return False

    def sym(root1, root2):
        '''
        判断两分支是否对称
        '''
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return sym(root1.left, root2.right) and sym(root1.right, root2.left)

    return sym(root.left, root.right)