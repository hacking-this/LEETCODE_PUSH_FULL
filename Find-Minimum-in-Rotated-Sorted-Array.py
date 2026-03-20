1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums)-1
5        ans = 5001
6        while left<right:
7            mid = (left+right)//2
8            if nums[mid]>nums[right]:
9                left = mid+1
10            else:
11                right = mid
12        return nums[left]
13
14