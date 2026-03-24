1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        left = 0
4        window_sum = 0
5        min_len = 10**6
6        for right in range(len(nums)):
7            window_sum+=nums[right]
8            while window_sum>=target:
9                min_len = min(min_len, right-left+1)
10                window_sum-=nums[left]
11                left+=1
12        if min_len==10**6:
13            return 0
14        else:
15            return min_len
16                