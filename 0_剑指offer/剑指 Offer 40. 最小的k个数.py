# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:57 AM 7/22/20
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

"""
import json
from typing import List
import collections
import heapq
import random

class Solution:
    # 前k个最小 用最大堆， 因为堆顶最大，比堆顶小的数就替换掉堆顶，然后还是k个最小；
    # 前k个最大 用最小堆， 因为堆顶最小，比堆顶大的就替换掉堆顶，重新排，这样堆整体变大了，最后就找到k个最大值。
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:  # arr后面的数比heap里最小的还要小
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

# 快排 1 单向
class Solution2:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k - num)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]

# 快排
class Solution3:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(low, high):
            i = low - 1
            pivot = arr[high]
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i] # 如果<= pivot,那么保持原样（自己和自己交换）。 如果出现 >pivot的值，暂时跳过，i不增加，找到下一个 <=pivot的值，i+1(那个大于pivot的值) 然后与j（小于pivot）交换
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1

        def myqs(low, high):
            if low < high:
                pivot = partition(low, high)
                if pivot == k: return
                if pivot > k - 1: myqs(low, pivot - 1)
                if pivot < k - 1: myqs(pivot + 1, high)

        myqs(0, len(arr) - 1)
        return arr[:k]


# 快排 2 双向
class Solution4: # https://www.cnblogs.com/AlwinXu/p/5424905.html
    def quickSort(self, mylist, start, end):
        if start < end:
            i, j = start, end
            pivot = mylist[j]
            while i < j:
                while (i < j) and mylist[i] <= pivot:
                    i += 1
                mylist[j] = mylist[i]

                while (i < j) and mylist[j] >= pivot:
                    j -= 1
                mylist[i] = mylist[j]

            mylist[i] = pivot
            self.quickSort(mylist, start, i - 1)
            self.quickSort(mylist, j + 1, end)
        return mylist

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        res = self.quickSort(arr, 0, len(arr) - 1)
        return res[:k]

# 快排 3 双向 https://www.cnblogs.com/bonelee/p/11789330.html
class Solution5: # https://zhuanlan.zhihu.com/p/139340733
    def quickSort(self, mylist, start, end):
        if start < end:
            i, j = start, end
            pivot = mylist[j]
            while i < j:
                while (i < j) and mylist[i] <= pivot:  # i和j相等 跳出while
                    i += 1

                while (i < j) and mylist[j] >= pivot:  # i和j相等 跳出while
                    j -= 1
                mylist[i], mylist[j] = mylist[j], mylist[i]

            mylist[i], mylist[end] = mylist[end], mylist[i] # i和j相等时， 与pivot交换
            self.quickSort(mylist, start, j - 1)
            self.quickSort(mylist, i + 1, end)
        return mylist

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        res = self.quickSort(arr, 0, len(arr) - 1)
        return res[:k]


class Solution6:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


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
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            arr = stringToIntegerList(line);
            line = next(lines)
            k = int(line);

            ret = Solution3().getLeastNumbers(arr, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()