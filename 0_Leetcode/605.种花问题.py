# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:57 AM 1/1/21
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数n。能否在不打破种植规则的情况下种入n朵花？能则返回True，不能则返回False。

示例 1:
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

示例 2:
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False

注意:
数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool: # Time: O(n)   Space: O(1)
        length = len(flowerbed)
        count = 0
        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
        return count >= n


    def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool: # Time: O(n)   Space: O(1)
        length = len(flowerbed)
        count = 0
        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
            if count >= n: return True
        return False

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        bed = [0] + flowerbed + [0]
        for i in range(1, length+1):
            if bed[i] == bed[i-1] == bed[i+1] == 0:
                bed[i] = 1
                n -= 1
            if n <= 0: return True
        return False

def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            flowerbed = stringToIntegerList(line);
            line = next(lines)
            n = int(line);

            ret = Solution().canPlaceFlowers(flowerbed, n)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()