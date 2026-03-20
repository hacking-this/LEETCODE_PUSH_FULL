1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        left = 0
4        right = len(letters)-1
5        ans = letters[0]
6        while left<=right:
7            mid = (left+right)//2
8            if letters[mid]>chr(ord(target)):
9                ans = letters[mid]
10                right = mid-1
11            else:
12                left = mid+1
13        return ans
14
15        