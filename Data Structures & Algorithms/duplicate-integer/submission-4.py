class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for n in nums:
            if n in store:
                return True
            else:
                store.add(n)
        return False
