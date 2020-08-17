# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:56 AM 7/22/20
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

"""
import json
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 当使用 self 时，是需要将变量用作某函数的全局变量。而在 python 中，数字需要加 self 才能实现，而列表不加、加都可以
        c, res = list(s), []  # c: ABC -> ['A', 'B', 'C']

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))
                return
            dic = set()  # 这个set只是保证此函数中开启的下轮递归 没有重复
            for i in range(x, len(c)):
                if c[i] in dic: continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 固定 c[i]为当前位字符
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]  # 还原之前的交换

        dfs(0)
        return res


def stringToString(input):
    return input[1:-1]

def stringArrayToString(input):
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
            s = stringToString(line)

            ret = Solution().permutation(s)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()