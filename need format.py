class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 判断以root2为根节点的树是否包含在以root1为根节点的树中
def has_substruct(root1, root2):
    if root1 is None or root2 is None:  # 左右任一根节点空则失匹，因为空树不算子结构
        return False
    if root1.val != root2.val:
        return False
    else:
        # 首先从根节点判断是否左边包含右边
        return (contain_rec(root1, root2) or
                has_substruct(root1.left, root2) or
                has_substruct(root1.right, root2))


# 递归判断左节点是否包含右节点，并且空树的处理由has_substruct()完成
# 所以这里当右节点为空时应该返回True
def contain_rec(node1, node2):
    if node2 is None:
        return True
    if node1 is None or node1.val != node2.val:
        return False
    return contain_rec(node1.left, node2.left) and contain_rec(node1.right, node2.right)
