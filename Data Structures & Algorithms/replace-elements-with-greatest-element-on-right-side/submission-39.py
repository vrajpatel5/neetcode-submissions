class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        start = 1
        end = len(arr)

        while i < end - 1:
            maxn = max(arr[start:end])
            arr[i] = maxn
            i += 1
            start += 1

        arr[end - 1] = -1
        
        return arr



            
        
