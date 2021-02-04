import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.valToIndex = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.valToIndex:
            return False
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True




    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.valToIndex:
            return False
        index = self.valToIndex[val]
        self.valToIndex[self.nums[-1]] = index  # 将最后一个元素对应的索引修改为 index
        self.nums[index], self.nums[-1] = self.nums[-1],  self.nums[index] # index位置的数字  和  最后一个数字 交换
        self.nums.pop()
        self.valToIndex.pop(val)
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums)-1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()