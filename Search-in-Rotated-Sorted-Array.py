1class Solution:
2    def search(self, arr: List[int], target: int) -> int:
3        left = 0
4        right = len(arr)-1
5        if len(arr)==1 and arr[0]==target:
6            return 0
7        elif len(arr)==1 and arr[0]!=target:
8            return -1
9        else:
10            while left<=right:
11                mid = (left+right)//2
12                if arr[mid]==target:
13                    return mid
14                # Find the sorted part
15                elif arr[left]<=arr[mid]:
16                    if arr[left]<=target<arr[mid]:
17                        right = mid-1
18                    else:
19                        left = mid+1
20                else:
21                    if arr[mid]<target<=arr[right]:
22                        left = mid+1
23                    else:
24                        right = mid-1
25        return -1
26
27        