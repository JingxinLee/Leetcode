# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:42 AM 2/4/21
### [752\. 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock/)

Difficulty: **中等**


你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'` 。每个拨轮可以自由旋转：例如把 `'9'` 变为  `'0'`<font face="Helvetica Neue, Helvetica, Arial, sans-serif" color="#333333" style="display: inline;"><span style="background-color: rgb(255, 255, 255); font-size: 14px; display: inline;">，</span></font>`'0'` 变为 `'9'` 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 `'0000'` ，一个代表四个拨轮的数字的字符串。

列表 `deadends` 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 `target` 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

**示例 1:**

```
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
```

**示例 2:**

```
输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。
```

**示例 3:**

```
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。
```

**示例 4:**

```
输入: deadends = ["0000"], target = "8888"
输出：-1
```

**提示：**

1.  死亡列表 `deadends` 的长度范围为 `[1, 500]`。
2.  目标数字 `target` 不会在 `deadends` 之中。
3.  每个 `deadends` 和 `target` 中的字符串的数字会在 10,000 个可能的情况 `'0000'` 到 `'9999'` 中产生。


"""
import json
from typing import List


class Solution:
    def plusOne(self, s, j):
        ch = list(s)
        if ch[j] == '9':
            ch[j] = '0'
        else:
            ch[j] = str(int(ch[j]) + 1) # 注意字符串的操作, 先用int做加法,最后转换乘str
        return ''.join(ch)

    def minusOne(self, s, j):
        ch = list(s)
        if ch[j] == '0':
            ch[j] = '9'
        else:
            ch[j] = str(int(ch[j]) - 1)
        return ''.join(ch)

    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set()
        for deadend in deadends:
            dead.add(deadend)
        visited = set()
        step = 0
        q = deque()
        q.append("0000")
        visited.add("0000")

        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()

                if cur in dead: # 在deadlock中的就要跳过
                    continue
                if cur == target: # 找到了
                    return step

                    # 将一个节点的未遍历相邻节点加入队列
                for j in range(4):
                    up = self.plusOne(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)

                    down = self.minusOne(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            step += 1
        return -1


def stringToStringArray(input):
    return json.loads(input)


def stringToString(input):
    return input[1:-1].decode('string_escape')


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            deadends = stringToStringArray(line)
            line = next(lines)
            target = stringToString(line)

            ret = Solution().openLock(deadends, target)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()