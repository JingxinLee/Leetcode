# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:03 PM 1/19/21
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：
    - LFUCache(int capacity) - 用数据结构的容量capacity 初始化对象
    - int get(int key)- 如果键存在于缓存中，则获取键的值，否则返回 -1。
    - void put(int key, int value)- 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。
      在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。

注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

进阶：
你是否可以在O(1)时间复杂度内执行两项操作？


示例：

输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);
lFUCache.put(2, 2);
lFUCache.get(1);      // 返回 1
lFUCache.put(3, 3);   // 去除键 2
lFUCache.get(2);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
lFUCache.put(4, 4);   // 去除键 1
lFUCache.get(1);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
lFUCache.get(4);      // 返回 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections

class LFUCache:

    def __init__(self, capacity: int):
        self.keyToVal = {}
        self.keyToFreq = {}
        self.freqToKeys = {}
        self.capacity = capacity
        self.minFreq = 0

    def get(self, key: int) -> int:
        # key不存在返回-1,否则增加freq 1次,返回key对应的值
        if key not in self.keyToVal or self.capacity == 0:
            return -1
        self.increaseFreq(key)
        return self.keyToVal[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return -1
        # 如果存在key,就只修改value,并且增加freq 1次
        if key in self.keyToVal:
            self.keyToVal[key] = value
            self.increaseFreq(key)
            return

        # key 不存在就要插入新key 和对应的value

        # 如果容量满了的话就得先淘汰minfreq对应的key
        if self.capacity <= len(self.keyToVal):
            self.removeMinFreqKey()

        # 插入新key和value,对应freq+1
        self.keyToVal[key] = value
        self.keyToFreq[key] = 1
        # 插入FKS表
        if 1 not in self.freqToKeys:
            self.freqToKeys[1] = []
        self.freqToKeys[1].append(key)

        self.minFreq = 1

    def increaseFreq(self, key):
        freq = self.keyToFreq[key]
        self.keyToFreq[key] = freq + 1
        # 将key从之前freq对应的列表中删除
        self.freqToKeys[freq].remove(key)
        # 将key加入 freq + 1 对应的列表中
        if freq + 1 not in self.freqToKeys:
            self.freqToKeys[freq + 1] = []
        self.freqToKeys[freq + 1].append(key)

        if self.freqToKeys[freq] == []:
            self.freqToKeys.pop(freq)
            if freq == self.minFreq:       # ???
                self.minFreq += 1

    def removeMinFreqKey(self):
        # freq 最小的 key 列表
        keyList = self.freqToKeys[self.minFreq]
        # 最先插入的key就是要被删除的key
        deletedKey = keyList[0]
        keyList.remove(deletedKey)
        if keyList == []:
            self.freqToKeys.pop(self.minFreq)

        # 更新KV KF表
        self.keyToVal.pop(deletedKey)
        self.keyToFreq.pop(deletedKey)

# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.get(3)