class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        ndict = {}

        for i in nums:
            if i in ndict:
                return ndict[i]
            ndict[i] = True
        return False