# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:01 PM 7/28/20

给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
"""
import json
from types import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        """
        主对角线全为１，分为上三角和下三角２部分
        """
        ｂ, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a)-2, -1, -1):
            tmp *= a[i + 1] # 依次为　×５　×５×４　×５×４×３　　×５×４×３×２
            b[i] *= tmp
        return b

def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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
            a = stringToIntegerList(line);

            ret = Solution().constructArr(a)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()