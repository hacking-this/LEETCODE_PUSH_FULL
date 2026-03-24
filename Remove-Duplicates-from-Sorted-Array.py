1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        left = 0
4        for right in range(1,len(nums)):
5            if nums[left]!=nums[right]:
6                left+=1
7                nums[left] = nums[right]
8        return left+1
9
10        