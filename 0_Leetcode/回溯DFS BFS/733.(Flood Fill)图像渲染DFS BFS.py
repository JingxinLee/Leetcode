# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:31 PM 1/31/21
### [733\. 图像渲染](https://leetcode-cn.com/problems/flood-fill/)

Difficulty: **简单**


有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标`(sr, sc)`表示图像渲染开始的像素值（行 ，列）和一个新的颜色值`newColor`，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标 [相同] 的相连像素点，
接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标 [相同] 的相连像素点，……，重复该过程。
将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

**示例 1:**

```
输入:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析:
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。
```

**注意:**

*   `image` 和`image[0]`的长度在范围`[1, 50]` 内。
*   给出的初始点将满足`0 <= sr < image.length` 和`0 <= sc < image[0].length`。
*   `image[i][j]` 和`newColor`表示的颜色值在范围`[0, 65535]`内。

"""
import json
from typing import List
from queue import Queue

class Solution: # DFS 使用递归
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] != newColor:
            old, image[sr][sc] = image[sr][sc], newColor
            for sri, scj in zip((sr, sr, sr+1, sr-1), (sc+1, sc-1, sc, sc)):
                if 0 <= sri < len(image) and 0 <= scj < len(image[0]) and image[sri][scj] == old:
                    self.floodFill(image, sri, scj, newColor)
        return image

class Solution1: # DFS 使用栈
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        stack = []
        stack.append((sr, sc))
        originalColor = image[sr][sc]
        while stack:
            point = stack.pop()
            image[point[0]][point[1]] = newColor
            for direction in directions:
                new_i = point[0] + direction[0]
                new_j = point[1] + direction[1]
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == originalColor:
                    stack.append((new_i, new_j))
        return image


class Solution3: # BFS 使用Queue
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]: # 起始颜色和目标颜色相同，则直接返回原图
            return image
        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        queue = Queue() # 构造一个队列，先把起始点放进去
        queue.put((sr, sc))
        originalColor = image[sr][sc]  # 记录初始颜色
        while not queue.empty():
            point = queue.get()  # 取出队列的点并染色
            image[point[0]][point[1]] = newColor

            for direction in directions:   # 遍历四个方向, 对四个方向的点进行处理,如果颜色和原来相同就加入queue中等待染色
                new_i = point[0] + direction[0]
                new_j = point[1] + direction[1]
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == originalColor:
                    queue.put((new_i, new_j))
        return image








def stringToInt2dArray(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            image = stringToInt2dArray(line)
            line = next(lines)
            sr = stringToInt(line)
            line = next(lines)
            sc = stringToInt(line)
            line = next(lines)
            newColor = stringToInt(line)

            ret = Solution().floodFill(image, sr, sc, newColor)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()