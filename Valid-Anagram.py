1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        hashmap_s = {}
4        hashmap_t = {}
5        if len(s)!=len(t):
6            return False
7        else:
8            for ch in s:
9                hashmap_s[ch] = hashmap_s.get(ch,0)+1
10            for ch in t:
11                hashmap_t[ch] = hashmap_t.get(ch,0)+1
12            return hashmap_s==hashmap_t
13
14        