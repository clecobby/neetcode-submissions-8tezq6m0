class Solution:
    def twoSum(self, nums: List[int], target:int)->List:
        remainder = {}

        for i, v in enumerate(nums):
            bal = target - v
            if bal in remainder :
                return [remainder[bal],i]
            remainder[v] = i