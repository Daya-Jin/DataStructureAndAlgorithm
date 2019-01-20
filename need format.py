class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, x):
        self.items.insert(0, x)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()


# 使用循环与栈来模拟递归
# 先将根节点入栈，然后类似层次遍历，左右子节点入栈
# 每弹出一个节点，交换其左右子节点
def mirror_tree(root_node):
    if root_node is None:  # 空树判断
        return root_node

    stack = Stack()
    stack.push(root_node)  # 根节点入栈

    while stack.size > 0:
        node = stack.pop()
        node.left, node.right = node.right, node.left  # 镜像翻转子节点
        # 再把子节点入栈
        if node.left:
            stack.push(node.left)
        if node.right:
            stack.push(node.right)
