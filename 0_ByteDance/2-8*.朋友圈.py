# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:24 PM 9/9/20
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
你必须输出所有学生中的已知的朋友圈总数。



示例 1：
输入：
[[1,1,0],
 [1,1,0],
 [0,0,1]]

输出：2
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。

示例 2：
输入：
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出：1
解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，
所以他们三个在一个朋友圈，返回 1 。

提示：
1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]
"""
import json

class Solution(object):
    def findCircleNum(self, M): # DFS 1
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        count = 0
        visited = set()

        def dfs(i):
            for j in range(N):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)
        for i in range(N):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        return count

class Solution2(object):
    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)

    def findCircleNum(self, M): # DFS 2
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                visited[i] = 1
                self.dfs(M, visited, i)
                count += 1
        return count

class Solution3(object): # BFS 1
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N, visited, res = len(M), set(), 0
        for i in range(N):
            if i not in visited:
                queue = [i]
                while queue:
                    p = queue.pop(0)
                    if p not in visited:
                        visited.add(p)
                        #queue += [k for k, num in enumerate(M[p]) if num and k not in visited]
                        for k,num in enumerate(M[p]):
                            if num and k not in visited:
                                queue += [k]
                res += 1
        return res
class Solution4: # BFS 2
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)  ##节点数量
        vis = set() ##访问过的节点记录
        ans = 0    ##连通分量计数
        for i in range(n):    ##遍历所有节点，作为搜索起点
            if i not in vis:  ##只处理没有访问过的节点
                queue = deque([i])    ##将首节点加入队列
                vis.add(i)    ##每加入一次队列，记录一次访问

                while queue:##bfs过程
                    q = queue.popleft()
                    for j in range(n):
                        if M[q][j] == 1 and j not in vis:  ##加入队列之前先检查一次是否访问过
                            queue.append(j)
                            vis.add(j)
                ans += 1
        return ans

def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


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
            M = stringToInt2dArray(line)

            ret = Solution3().findCircleNum(M)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()