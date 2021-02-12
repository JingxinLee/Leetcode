# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:33 PM 1/31/21
### [17\. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

Difficulty: **中等**


给定一个仅包含数字`2-9`的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png)

**示例 1：**

```
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**示例 2：**

```
输入：digits = ""
输出：[]
```

**示例 3：**

```
输入：digits = "2"
输出：["a","b","c"]
```

**提示：**

*   `0 <= digits.length <= 4`
*   `digits[i]` 是范围 `['2', '9']` 的一个数字。

"""
import json
from typing import List



class Solution0:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        combination = []
        combinations = []

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
                return

            digit = digits[index]
            for letter in mapping[digit]:
                combination.append(letter)
                backtrack(index + 1)
                combination.pop()

        backtrack(0)
        return combinations

class Solution1: # 和上一个方法一样,只是不一样的写法罢了
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        combination = []
        combinations = []
        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in mapping[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()
        backtrack(0)
        return combinations

class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        mapping = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }
        res = []
        def dfs(curStr, i): # curStr是当前字符串，i是扫描的指针
            if i >= len(digits): # 指针越界，递归的出口
                res.append(curStr) # 将解推入res
                return  # 结束当前递归分支
            letters = mapping[digits[i]] # 当前数字对应的字母
            for letter in letters: # 一种字母对应一个递归分支
                dfs(curStr + letter, i + 1) # 生成新字符串，i指针右移，递归   curStr + letter 相当于上一解的两步 => append 和 pop
        dfs('', 0)  # 递归的入口，初始字符串为''，指针为0
        return res

import collections
class Solution3: # BFS
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        que = collections.deque()
        que.append('')
        for i in range(len(digits)):
            len_que = len(que)
            for j in range(len_que):
                cur_digit = mapping[digits[i]]
                cur_que_digit = que.popleft()
                for digit in cur_digit:
                    que.append(cur_que_digit + digit)
            #print('当前队列中的内容: ', que)
        return list(que)

from queue import Queue
class Solution: # 队列 BFS
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        que = collections.deque()
        que.append('')
        for i in range(len(digits)):
            cur_digit = mapping[digits[i]]
            for j in range(len(que)):
                cur_que_digit = que.popleft()
                for digit in cur_digit:
                    que.append(cur_que_digit + digit)
            #print('当前队列中的内容: ', que)
        return list(que)

class Solution4: # 队列 BFS
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit)-50]:# 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue

def stringToString(input):
    return input[1:-1]

def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            digits = stringToString(line)

            ret = Solution().letterCombinations(digits)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()