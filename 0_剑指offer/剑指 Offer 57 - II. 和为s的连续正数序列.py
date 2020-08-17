# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:18 PM 7/26/20

输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""
import json

class Solution(object):
    def findContinuousSequence(self, target): # https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/nei-cun-xiao-hao-153mzhan-sheng-100de-pythonyong-h/
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i, j = 1, 2
        ans = []
        while i < target and j < target:
            sum = int((i + j) * (j - i + 1) / 2)
            if sum < target:
                j += 1
            elif sum > target:
                i += 1
            else:
                ans.append(list(range(i, j + 1)))
                i += 1
                j += 1
        return ans

    def findContinuousSequence2(self, target): # https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
        """
        # 滑 动 窗 口
        :type target: int
        :rtype: List[List[int]]
        """
        i, j, sum, res = 1, 1, 0, [] # sum是滑动窗口中数字的和
        while i <= target // 2: # 两个比target/2大的数加起来，一定比target大
            if sum < target:
                sum += j
                j += 1
            elif sum > target:
                sum -= i
                i += 1
            else:
                res.append(list(range(i, j)))
                sum -= i
                i += 1
        return res



def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            target = stringToInt(line)

            ret = Solution().findContinuousSequence(target)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()