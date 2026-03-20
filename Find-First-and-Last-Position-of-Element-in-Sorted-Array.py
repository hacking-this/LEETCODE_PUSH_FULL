1class Solution:
2    def searchRange(self, arr: List[int], target: int) -> List[int]:
3        left = 0
4        right = len(arr)-1
5        min = -1
6        while left<=right:
7            mid = (left+right)//2
8            if arr[mid]==target:
9                min = mid
10                right = mid-1
11            elif arr[mid]>target:
12                right = mid-1
13            else:
14                left = mid + 1
15        low = 0
16        high = len(arr)-1
17        max = -1
18        while low<=high:
19            mid = (low+high)//2
20            if arr[mid]==target:
21                max = mid
22                low = mid+1
23            elif arr[mid]>target:
24                high = mid-1
25            else:
26                low = mid+1 
27        return [min,max]
28        
29        
30        
31
32        