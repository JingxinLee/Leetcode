# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 2:49 PM 1/22/21

"""
import json
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            # 这里不能用dic[key] : 因为get() method returns a default value if the key is missing.
            # However, if the key is not found when you use dict[key], KeyError exception is raised
            if dic.get(target - num) is not None:
                return [dic[target - num], i]
            dic[num] = i

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
        for line in io.TextIOWrapper(sys.stdin.buffer):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);

            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()