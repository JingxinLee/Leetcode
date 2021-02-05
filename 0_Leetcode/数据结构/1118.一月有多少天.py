# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 4:11 PM 1/20/21
指定年份Y 和月份M，请你帮忙计算出该月一共有多少天。

示例 1：
输入：Y = 1992, M = 7
输出：31

示例 2：
输入：Y = 2000, M = 2
输出：29

示例 3：
输入：Y = 1900, M = 2
输出：28

提示：
1583 <= Y <= 2100
1 <= M <= 12

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-days-in-a-month
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import json
from typing import List

class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
            return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][M-1]
        else:
            return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][M-1]


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
            Y = int(line);
            line = next(lines)
            M = int(line);

            ret = Solution().numberOfDays(Y, M)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()