# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 下午3:27 2020/7/7
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释:因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例3:

输入:
s = "ab"
p = ".*"
输出: true
解释:".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释:因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s可能为空，且只包含从a-z的小写字母。
p可能为空，且只包含从a-z的小写字母以及字符.和*，无连续的 '*'。
https://www.bilibili.com/video/BV1Tt4y1U7QP
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if not p: return not s
        cache = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        cache[0][0] = True
        for i in range(1, len(p)):
            cache[i + 1][0] = cache[i - 1][0] and p[i] == '*'  # cache[i+1] 对应的是 p[i]
        for i in range(len(p)):
            for j in range(len(s)):
                print('p[i]= ', p[i])
                print('s[j]= ', s[j])
                if p[i] == '*':
                    cache[i + 1][j + 1] = cache[i][j + 1] or cache[i - 1][j + 1]  # * 与上面2结果有关
                    print('p[i-1]= ', p[i-1])
                    print('s[j]= ', s[j])
                    if p[i - 1] == s[j] or p[i - 1] == '.':  # * 前一个 与 s的第j个相等的话, 结果与左边 取或
                        cache[i + 1][j + 1] |= cache[i + 1][j]
                else:
                    cache[i + 1][j + 1] = cache[i][j] and (p[i] == s[j] or p[i] == '.') # 其他的与左上角有关
        return cache[-1][-1]


def stringToString(input):
    return input[1:-1]

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
            s = stringToString(line);
            line = next(lines)
            p = stringToString(line);

            ret = Solution().isMatch(s, p)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()