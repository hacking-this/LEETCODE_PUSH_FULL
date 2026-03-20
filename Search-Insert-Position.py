1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums)-1
5        while left<=right:
6            mid = (left+right)//2
7            if nums[mid]==target:
8                return mid
9            elif nums[mid]>target:
10                right = mid-1
11            else:
12                left = mid + 1
13        return left
14
15        