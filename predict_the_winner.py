import math
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        gain = [[None for i in range(len(nums))] for k in range(len(nums))]
        for k in range(len(nums)):
            i=0
            while i+k<len(nums):
                if k == 0:
                    gain[i][i + k] = nums[i]
                elif k == 1:
                    gain[i][i + k] = abs(nums[i] - nums[i + k])
                else:
                    gain[i][i + k] = max(gain[i][i] - gain[i + 1][i + k], gain[i + k][i + k] - gain[i][i + k - 1])
                i+=1
        return gain[0][len(nums) - 1] >= 0
