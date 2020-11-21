class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.nxt = None


class LRU_cache:
    def __init__(self, _capacity: int):
        self._capacity = _capacity

        # 哈希表
        self._cache = dict()

        # 双向链表，_head指向最常用，_tail指向最不常用
        self._head = None
        self._tail = None

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        node = self._cache[key]
        val = node.val
        self._del(node)
        self._add(key, val)

        return val

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._del(self._cache[key])
        elif len(self._cache) == self._capacity:
            self._del(self._tail)  # 删除节点

        self._add(key, value)

    def _add(self, key, val):
        node = Node(key, val)
        self._cache[key] = node

        node.pre = None
        node.nxt = self._head

        if not self._head:
            self._tail = node
        else:
            self._head.pre = node

        self._head = node

    def _del(self, node: Node):
        pre, nxt = node.pre, node.nxt

        if not pre:  # 待删节点为首节点
            self._head = nxt
        else:
            pre.nxt = nxt

        if not nxt:  # 待删节点为尾节点
            self._tail = pre
        else:
            nxt.pre = pre

        del self._cache[node.key]
        del node


if __name__ == "__main__":
    obj = LRU_cache(2)
    obj.put(2, 6)
    obj.put(1, 5)
    obj.put(1, 2)
    print(obj.get(1))
    print(obj.get(2))
