class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # use a dictionary to store the already searched items
        hist = {}

        for i, n in enumerate(nums):
            if target - n in hist:
                return [hist[target-n], i]
            
            hist[n] = i