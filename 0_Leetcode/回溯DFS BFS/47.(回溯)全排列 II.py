# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:19 PM 1/30/21
### [47\. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

Difficulty: **中等**


给定一个可包含重复数字的序列 `nums` ，**按任意顺序** 返回所有不重复的全排列。

**示例 1：**

```
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

**示例 2：**

```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**提示：**

*   `1 <= nums.length <= 8`
*   `-10 <= nums[i] <= 10`

https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-ga-4/

https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
"""
import json
from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        track = []
        used = [False] * len(nums)
        nums.sort()
        self.backtrack(nums, track, used)
        return self.res

    def backtrack(self, nums, track, used):
        if len(track) == len(nums):
            self.res.append(track[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                # 当i可以选第一个元素之后的元素时(因为如果i=0，即只有一个元素，哪来的重复？有重复即说明起码有两个元素或以上,i>0)
                # 然后判断当前元素是否和上一个元素相同？
                # 如果相同，再判断[上一个元素是否能用] 如果上个元素没用,且这个元素又和上个元素相同,那么肯定会重复
                # 因为上个元素用了, 之后就不会用到了, 也就不会重复.上个元素没用, 那就还有可能用到, 导致重复
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                track.append(nums[i])
                used[i] = True
                self.backtrack(nums, track, used)
                used[i] = False
                track.pop()

def stringToIntegerList(input):
    return json.loads(input)


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
            nums = stringToIntegerList(line)

            ret = Solution().permuteUnique(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()