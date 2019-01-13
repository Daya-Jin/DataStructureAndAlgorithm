class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 设立三个指针，head，pre，cur，分别为头指针，最后一个非重复元素，工作指针
# 注意始终保持pre->cur的链接
def deleteDuplication(headnode):
    if headnode is None or headnode.next is None:  # 空链表或单节点链表
        return headnode

    pre = None
    cur = headnode  # 工作指针从头指针之前开始

    while cur:  # 节点非空
        if cur.next and cur.val == cur.next.val:  # 如果当前跟后继重复
            dump = cur.val
            while cur and cur.val == dump:  # 跳过所有等于重复值的节点
                if pre is None:  # 头结点重复
                    cur = cur.next
                    headnode = cur
                else:  # 中间节点重复
                    cur = cur.next
                    pre.next = cur
        else:  # 当前节点未重复
            pre = cur
            cur = cur.next

    return headnode
