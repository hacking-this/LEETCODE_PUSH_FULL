1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        collect = set()
4        left = 0
5        max_len = 0
6        for right in range(len(s)):
7            while s[right] in collect:
8                collect.remove(s[left])
9                left+=1
10            collect.add(s[right])
11            max_len = max(max_len,right-left+1)
12        return max_len
13
14
15
16
17            
18
19
20        