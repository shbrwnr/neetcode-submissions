class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        counter = 0
        for num in nums:
            if num == 0:
                output = max(output, counter)
                counter = 0 
            else:
                counter += 1
        return max(counter, output)