idx = 0
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: list
    :rtype: TreeNode
    """
    global idx
    if not data or data == ['null']:
        return None

    if idx < len(data):
        if data[idx] == 'null':
            idx += 1
            return None
        else:
            new_node = TreeNode(int(data[idx]))
            idx += 1
            new_node.left = deserialize(data)
            new_node.right = deserialize(data)
            return new_node


deserialize(['1', '2', '3', 'null', 'null', '4', '5'])