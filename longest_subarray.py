class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        minQue, maxQue = deque(), deque()
        for num in nums:
            while minQue and minQue[-1] > num: minQue.pop()
            while maxQue and maxQue[-1] < num: maxQue.pop()
            minQue.append(num)
            maxQue.append(num)
            if maxQue[0] - minQue[0] > limit:
                if nums[i] == minQue[0]: minQue.popleft()
                if nums[i] == maxQue[0]: maxQue.popleft()
                i += 1
        return len(nums) -i
