class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminder = {}

        for i,v in enumerate (nums):
            remain= target -v 
            if remain in reminder:
                return [reminder[remain],i]
            reminder[v]= i
