1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        arr = []
5        for i in range(len(nums)):
6            if i>0 and nums[i]==nums[i-1]:
7                continue
8            
9            left = i+1
10            right = len(nums)-1
11
12            while left<right:
13                total = nums[i]+nums[left]+nums[right]
14                if total==0:
15                    arr.append([nums[i],nums[left],nums[right]])
16                    left+=1
17                    right-=1
18                    #SKIP DUPLICATES
19                    while left<right and nums[left]==nums[left-1]:
20                        left+=1
21                    while left<right and nums[right]==nums[right+1]:
22                        right-=1
23                elif total<0:
24                    left+=1
25                else:
26                    right-=1
27        return arr
28
29        