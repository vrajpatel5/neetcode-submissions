class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numdict = {}

        for index, num in enumerate(nums):
            comp = target - num
            if comp in numdict:
                return [numdict[comp], index]
            
            numdict[num] = index