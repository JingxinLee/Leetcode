# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:57 AM 7/22/20
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

初始化： 票数统计 votes = 0 ， 众数 x；
循环： 遍历数组 nums 中的每个数字 num ；
当 票数 votes 等于 0 ，则假设当前数字 num 是众数；
当 num = x 时，票数 votes 自增 1 ；当 num != x 时，票数 votes 自减 1 ；
返回值： 返回 x 即可；

作者：jyd
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
import json
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return None
        votes, x = 0, nums[0]
        for num in nums:
            if votes == 0:
                x = num  # votes为0时， 设置众数为当前num
            votes += 1 if num == x else -1
            # if numm == x: votes += 1
            # else votes -= 1
        return x


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return None
        dic = {}
        max_count, max_num = 0, nums[0]
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

            if dic[num] > max_count:
                max_count = dic[num]
                max_num = num
        return max_num

def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))


    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().majorityElement(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()