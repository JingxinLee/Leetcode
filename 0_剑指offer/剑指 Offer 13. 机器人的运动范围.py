# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 下午12:52 2020/7/5
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3 => [0,0] [0,1] [1,0]

示例 2：
输入：m = 3, n = 1, k = 0
输出：1 => [0,0]

提示：
1 <= n,m <= 100
0 <= k<= 20
"""
import json

# 数 位 之 和 计 算
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)
# BFS
class Solution2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue, visited = [(0,0,0,0)], set()
        while queue:
            i,j,si,sj = queue.pop(0)
            if i >= m or j >= n or si+sj >  k or (i,j) in visited:
                continue
            visited.add((i,j))
            queue.append((i+1,j,si+1 if(i+1)%10 else si-8, sj)) # 先入先出
            queue.append((i,j+1,si, sj+1 if(j+1)%10 else sj-8))
        return len(visited)
# DFS
class Solution3:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or si + sj > k or (i, j) in visited:
                return False
            visited.add((i, j))
            return 1 + dfs(i+1, j, si+1 if (i+1)%10 else si-8, sj) + dfs(i, j+1, si, sj+1 if (j+1)%10 else sj-8)
        visited = set()
        return dfs(0,0,0,0)

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
            m = int(line);
            line = next(lines)
            n = int(line);
            line = next(lines)
            k = int(line);

            ret = Solution().movingCount(m, n, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()