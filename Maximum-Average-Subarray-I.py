1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        window_sum = sum(nums[:k])
4        max_sum = window_sum
5        for i in range(k,len(nums)):
6            # window_sum = window_sum + nums[i]
7            # window_sum = window_sum - nums[i-k]
8            window_sum += nums[i] - nums[i-k]
9            max_sum = max(max_sum,window_sum)
10        return max_sum/k
11        