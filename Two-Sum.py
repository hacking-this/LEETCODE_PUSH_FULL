1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hashmap = {}
4        for i in range(len(nums)):
5            complement = target - nums[i]
6            if complement in hashmap:
7                return [hashmap[complement],i]
8            else:
9                hashmap[nums[i]]=i
10        
11                
12        
13
14