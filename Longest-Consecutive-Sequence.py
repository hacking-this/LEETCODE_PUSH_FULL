1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        max_count = 0
5        for num in num_set:
6            if num-1 not in num_set:
7                current = num
8                count = 1
9                while current+1 in num_set:
10                    count+=1
11                    current+=1
12                max_count=max(max_count,count)
13        return max_count
14
15
16        