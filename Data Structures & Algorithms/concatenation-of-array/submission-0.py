class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        dup_nums = []

        for i in nums:
            dup_nums.append(i)
        
        return nums + dup_nums