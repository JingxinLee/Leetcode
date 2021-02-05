# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:48 PM 1/28/21
### [46\. 全排列](https://leetcode-cn.com/problems/permutations/)

Difficulty: **中等**


给定一个 **没有重复** 数字的序列，返回其所有可能的全排列。

**示例:**

```
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

  递归之前 => [1]
  递归之前 => [1, 2]
  递归之前 => [1, 2, 3]
递归之后 => [1, 2]
递归之后 => [1]
  递归之前 => [1, 3]
  递归之前 => [1, 3, 2]
递归之后 => [1, 3]
递归之后 => [1]
递归之后 => []
  递归之前 => [2]
  递归之前 => [2, 1]
  递归之前 => [2, 1, 3]
递归之后 => [2, 1]
递归之后 => [2]
  递归之前 => [2, 3]
  递归之前 => [2, 3, 1]
递归之后 => [2, 3]
递归之后 => [2]
递归之后 => []
  递归之前 => [3]
  递归之前 => [3, 1]
  递归之前 => [3, 1, 2]
递归之后 => [3, 1]
递归之后 => [3]
  递归之前 => [3, 2]
  递归之前 => [3, 2, 1]
递归之后 => [3, 2]
递归之后 => [3]
递归之后 => []
输出 => [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

：https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

```
https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-ga-4/

“排列”问题使用 used 数组来标识选择列表，

而“子集、组合”问题则使用 start 参数。

"""
import json
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, res, used):
            if depth ==  size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth+1, path, res, used)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0: return []
        res = []
        used = [False for _ in range(size)]
        dfs(nums, size, 0, [], res, used)
        return res

class Solution0:
    def __init__(self) -> None:
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.res

    def backtrack(self, nums, track, used):
        if len(track) == len(nums):
            self.res.append(track[:])
            return

        for i in range(len(nums)): # 固定了(选择了)某个数，那么他的下一层的选择列表就是  除去这个数以外的其他数 也就是还没有用使用过的
            if not used[i]: # 从给定的数中除去用过的，就是当前的选择列表.
                track.append(nums[i])
                used[i] = True  # 在考虑下一个位置的时候，就能够以 O(1) 的时间复杂度判断这个数是否被选择过
                self.backtrack(nums, track, used)
                used[i] = False
                track.pop()

class Solution1:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        self.backtrack(nums, track)
        return self.res

    def backtrack(self, nums, track):
        if len(track) == len(nums):
            self.res.append(track[:])  # 注意 是要 track[:], 而不只有track
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.backtrack(nums, track)
            track.pop()

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, track):
            if len(track) == len(nums):
                self.res.append(track[:])
                return
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()
        self.res, track = [], []
        backtrack(nums, track)
        return self.res



def stringToIntegerList(input):
    return json.loads(input)


def int2dArrayToString(input):
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
            nums = stringToIntegerList(line)

            ret = Solution().permute(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()