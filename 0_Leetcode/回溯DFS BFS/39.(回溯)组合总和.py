# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:31 PM 1/29/21
### [39\. 组合总和](https://leetcode-cn.com/problems/combination-sum/)

Difficulty: **中等**


给定一个**无重复元素**的数组`candidates`和一个目标数`target`，找出`candidates`中所有可以使数字和为`target`的组合。

`candidates`中的数字可以**无限制重复**被选取。

**说明：**

*   所有数字（包括`target`）都是正整数。
*   解集不能包含重复的组合。

**示例1：**

```
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
```

**示例2：**

```
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
 [2,2,2,2],
 [2,3,3],
 [3,5]
]
```

**提示：**

*   `1 <= candidates.length <= 30`
*   `1 <= candidates[i] <= 200`
*   `candidate` 中的每个元素都是独一无二的。
*   `1 <= target <= 500`

"""
import json
from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        track = []
        candidates.sort() # 要先排序
        self.backtrack(candidates, target, 0, 0, track)
        return self.res

    def backtrack(self, nums, target, start, sum, track):
        # 结束条件
        if sum == target: # 路径总和等于 target 时候，就应该把路径加入结果集，并 return
            self.res.append(track[:])
            return
        for i in range(start, len(nums)):
            # 剪 枝
            if sum > target: # 当前状态的sum大于target的时候就应该剪枝，不用再递归下去了
                continue # 也可以 return
            # 做 出 选 择
            track.append(nums[i])
            # 无 限 次 被 选 择，那么 i 就不用 +1 。即下一层的选择列表，从自身开始。并且要更新当前状态的sum
            self.backtrack(nums, target, i, sum+nums[i], track)
            # 撤 销 选 择
            track.pop()

def stringToIntegerList(input):
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
            candidates = stringToIntegerList(line)
            line = next(lines)
            target = stringToInt(line)

            ret = Solution().combinationSum(candidates, target)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()