1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        left = 0
4        right  = len(s)-1
5        while left<right:
6            while left<right and not s[left].isalnum():
7                left+=1
8            while left<right and not s[right].isalnum():
9                right-=1
10            if s[left].lower()==s[right].lower():
11                left+=1
12                right-=1
13            else:
14                return False
15        return True
16        
17        