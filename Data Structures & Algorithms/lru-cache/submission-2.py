class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> Node
        
        # 初始化双哨兵节点
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # ✂️ 完美的断开逻辑
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_to_tail(self, node):
        # 🔗 完美的插入队尾逻辑
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_to_tail(node) # 刷新新鲜度
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 情况 A：更新已有数据
            node = self.cache[key]
            node.val = value # 更新内容
            self._remove(node)
            self._insert_to_tail(node) # 刷新新鲜度
        else:
            # 情况 B：插入新数据
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_to_tail(new_node)
            
            # 🚨 触发淘汰机制
            if len(self.cache) > self.cap:
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]