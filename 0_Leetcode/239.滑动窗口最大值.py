# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 1:52 PM 1/2/21

给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。
滑动窗口每次只向右移动一位。 返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

示例 3：
输入：nums = [1,-1], k = 1
输出：[1,-1]

示例 4：
输入：nums = [9,11], k = 2
输出：[11]

示例 5：
输入：nums = [4,-2], k = 2
输出：[4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/
"""
import json
from typing import List
import heapq
import collections

class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]: # 暴力法
        n = len(nums)
        res = []
        for i in range(n - k +1):
            maxx = -float('inf')
            for j in range(i, i + k):
                if nums[j] > maxx:
                    maxx = nums[j]
            res.append(maxx)
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:  # 优先队列
        """
        时间复杂度：O(nlogn)，其中 n 是数组nums 的长度。在最坏情况下，数组 nums 中的元素单调递增，那么最终优先队列中包含了所有元素，没有元素被移除。
                  由于将一个元素放入优先队列的时间复杂度为 O(logn)，因此总时间复杂度为 O(nlogn)。

        空间复杂度：O(n)，即为优先队列需要使用的空间。这里所有的空间复杂度分析都不考虑返回的答案需要的 O(n) 空间，只计算额外的空间使用。

        """
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for j in range(k, n):
            heapq.heappush(q, (-nums[j], j))
            if q[0][1] <= j - k: # 用while 不是 if : 要把前面所有不在k范围内的都要pop掉
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:  # 单调队列
        n = len(nums)
        q = collections.deque() # q 保存下标
        # 将前k个值放入q
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]: # 下标对应的数值是递减的
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]

        for j in range(k, n):
            while q and nums[j] >= nums[q[-1]]:
                q.pop()
            q.append(j)
            while q[0] <= j - k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans



# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# print(maxSlidingWindow(nums, k))

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
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            k = int(line);

            ret = Solution().maxSlidingWindow(nums, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()