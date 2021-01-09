# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:00 AM 1/6/21

给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

示例 1：
输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]

示例 2：
输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]

示例 3：
输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]


提示：
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import json
from typing import List

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """


def stringToString2dArray(input):
    return json.loads(input)


def stringToDoubleList(input):
    return json.loads(input)


def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input


def doubleListToString(nums, len_of_list=None):
    if nums is None or len_of_list == 0:
        return "[]"

    if len_of_list is None:
        len_of_list = len(nums)

    serializedDoubles = []
    for num in nums:
        serializedDoubles.append(doubleToString(num))
    return "[{}]".format(','.join(serializedDoubles))


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            equations = stringToString2dArray(line)
            line = next(lines)
            values = stringToDoubleList(line)
            line = next(lines)
            queries = stringToString2dArray(line)

            ret = Solution().calcEquation(equations, values, queries)

            out = doubleListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()