1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        stack = []
4        hashmap={}
5
6        for num in nums2:
7            while stack and stack[-1]<=num:
8                hashmap[stack.pop()] = num
9            stack.append(num)
10        
11        while stack:
12            hashmap[stack.pop()] = -1
13
14        result = []
15        for i in range(len(nums1)):
16            result.append(hashmap[nums1[i]])
17            
18        return result
19