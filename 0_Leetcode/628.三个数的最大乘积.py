# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:40 PM 1/20/21
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。


示例 1：
输入：nums = [1,2,3]
输出：6

示例 2：
输入：nums = [1,2,3,4]
输出：24

示例 3：
输入：nums = [-1,-2,-3]
输出：-6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers/solution/python3-liang-chong-fang-fa-ji-suan-san-nae0f/

"""
import json
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[0] * nums[1] * nums[n - 1], nums[n - 1] * nums[n - 2] * nums[n - 3])

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = b = c = float('-inf')
        d = e = float('inf')
        for i, num in enumerate(nums):
            # 更新最大三个数
            if num > a:
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num
            # 更新最小两个数
            if num < d:
                d, e = num, d
            elif num < e:
                e = num

        return max(d * e * a, a * b * c)


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

            ret = Solution().maximumProduct(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()