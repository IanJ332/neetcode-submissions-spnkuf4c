class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- 辅助函数：操作双向链表的核心 ---

    def _add(self, node):
        """将节点插入到 head 后面（即链表头部，代表最新使用）"""
        nxt = self.head.next
        
        # 1. 处理 node 的连接
        node.next = nxt
        node.prev = self.head
        
        # 2. 处理 head 和原先第一个节点的连接
        self.head.next = node
        nxt.prev = node

    def _remove(self, node):
        """将节点从当前位置抠出来"""
        pre = node.prev
        nxt = node.next
        # 让前后邻居越过它直接牵手
        pre.next = nxt
        nxt.prev = pre

    # --- 主功能函数 ---

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)
        
        if len(self.cache) > self.capacity:
            # 找到最久没用的（tail的前一个）
            lru_node = self.tail.prev
            # 必须先删字典，再删链表
            del self.cache[lru_node.key]
            self._remove(lru_node)