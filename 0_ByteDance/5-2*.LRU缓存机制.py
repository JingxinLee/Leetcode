# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 12:16 PM 9/13/20
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
它应该支持以下操作： 获取数据 get 和 写入数据 put 。

- 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。

- 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；
如果关键字不存在，则插入该组「关键字/值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

删除 头节点，  添加 到尾部， 同时表明被访问过。
进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？


示例:
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""
class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # 哨兵节点
        self.sentinel = ListNode(None, None)
        # 尾节点
        self.tail = ListNode(None, None)
        # 初始化双向链表
        self.sentinel.next = self.tail
        self.tail.prev = self.sentinel


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 删除该节点
            self.remove_node_from_list(node)
            # 把该节点添加到链表头部
            self.push_node_to_front(node)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node_from_list(self.cache[key])
        node = ListNode(key, value)
        self.cache[key] = node
        self.push_node_to_front(node)

        # 如果链表超过最大容量， 删除链表尾部节点
        # 当缓存容量已满，我们不仅仅要删除最后一个 Node 节点，
        # 还要把 map 中映射到该节点的 key 同时删除，
        # 而这个 key 只能由 Node 得到。
        # 如果 Node 结构中只存储 val，那么我们就无法得知 key 是什么，
        # 就无法删除 map 中的键，造成错误
        if len(self.cache) > self.cap:
            last_node = self.tail.prev
            self.remove_node_from_list(last_node)
            self.cache.pop(last_node.key)

    def remove_node_from_list(self, node: "ListNode") -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.pre = prev

    def push_node_to_front(self, node: "ListNode") -> None:
        nxt = self.sentinel.next
        self.sentinel.next = node
        node.next = nxt
        node.prev = self.sentinel
        nxt.pre = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)