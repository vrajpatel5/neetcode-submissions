class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1s = 0
        count = 0
        # [1,1,0,1,1,1]

        for i in nums:
            if i == 0:
                count = 0
            
            if i == 1:
                count += 1
            
            max1s = max(count, max1s)

            
        return max1s