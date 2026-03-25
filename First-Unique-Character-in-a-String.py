1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3        freq = {}
4        for ch in s:
5            freq[ch] = freq.get(ch,0)+1
6        for i in range(len(s)):
7            if freq[s[i]]==1:
8                return i
9        return -1
10        