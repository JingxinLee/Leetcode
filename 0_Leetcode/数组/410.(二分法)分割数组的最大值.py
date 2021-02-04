# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:29 AM 1/24/21
给定一个非负整数数组和一个整数m，你需要将这个数组分成m个非空的连续子数组。设计一个算法使得这m个子数组各自和的最大值最小。

注意:
数组长度n满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

示例:
输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""
import json
from typing import List

class Solution:
    def split(self, nums, maxx): # 限制最大的子数组和为maxx
        count, num_sum = 1, 0
        for i in range(len(nums)):
            if num_sum + nums[i] > maxx:
                count += 1
                num_sum = nums[i]
            else:
                num_sum += nums[i]
        return count

    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = max(nums), sum(nums)+1
        while lo < hi:
            mid = lo + (hi -lo) // 2
            n = self.split(nums, mid)
            if n <= m: # 最大子数组和高了,减小一些. 收缩右边界
                hi = mid
            else:
                lo = mid + 1
        return lo



def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            m = int(line);

            ret = Solution().splitArray(nums, m)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()