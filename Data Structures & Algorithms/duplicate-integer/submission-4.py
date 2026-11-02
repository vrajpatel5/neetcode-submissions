class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        ndict = {}

        for i in nums:
            if i in ndict:
                return True
            ndict[i] = 1
        return False