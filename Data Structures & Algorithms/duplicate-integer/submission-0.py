class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        settings = set()
        for n in nums:
            if n in settings:
                return True
            settings.add(n)
        return False
            