# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午4:00 2020/7/7
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numbers = [str(i) for i in range(10)]
        n = len(s)

        e_show_up, dot_show_up, num_show_up, num_after_e = False, False, False, False

        for i in range(n):
            c = s[i]
            if c in numbers:
                num_show_up = True
                num_after_e = True
            elif c in ['+', '-']:
                if i > 0 and s[i-1] != 'e': # 如果不是开头, 且正负号前面不是e
                    return False
            elif c == '.':
                if dot_show_up or e_show_up: # 如果小数点和e都出现过,这时候再出现小数点就是错误的
                    return False
                dot_show_up = True
            elif c == 'e':
                if e_show_up or not num_show_up: # 如果e出现过 且 没有数字出现过
                    return False
                e_show_up = True
                num_show_up = False
            else:
                return False
        return num_show_up and num_after_e

a = Solution()
print(a.isNumber('+100'))