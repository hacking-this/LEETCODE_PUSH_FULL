1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        collector = set
4        result = []
5        collector = {}
6        for i, num in enumerate(nums):
7            complement = target - num
8
9            if complement in collector:
10                return [collector[complement], i]
11            collector[num] = i
12        
13
14