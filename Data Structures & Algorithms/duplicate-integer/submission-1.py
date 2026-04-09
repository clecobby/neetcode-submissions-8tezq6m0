class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for n in range (len(nums)):
            for nn in range (n+1,len(nums)):
                if nums[n]==nums[nn]:
                    return True
        return False