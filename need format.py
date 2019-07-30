import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(arr):
    if not arr:
        return None

    n = len(arr)
    if n == 1:
        return TreeNode(arr[0])

    root = TreeNode(arr[0])
    i=1
    while i<n:
        if arr[i] > arr[0]:
            break
        i+=1

    root.left = buildTree(arr[1:i])
    root.right = buildTree(arr[i:])
    return root


def levelTrav(root):
    res=list()
    if not root:
        return res

    q=[root]
    while q:
        level_size=len(q)
        for _ in range(level_size):
            vis_node=q.pop(0)
            res.append(vis_node.val)

            if vis_node.left:
                q.append(vis_node.left)
            if vis_node.right:
                q.append(vis_node.right)

    return res

root = buildTree(arr)
res=levelTrav(root)
print(res)
