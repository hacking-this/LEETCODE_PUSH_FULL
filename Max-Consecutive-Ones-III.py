1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        left = 0
4        max_len=-1
5        zero_count = 0
6        for right in range(len(nums)):
7            if nums[right]==0:
8                zero_count+=1
9            
10            while zero_count>k:
11                if nums[left]==0:
12                    zero_count-=1
13                left+=1
14            max_len = max(max_len,right-left+1)
15        return max_len
16                
17
18        