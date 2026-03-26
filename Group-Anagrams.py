1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        hashmap = {}
4
5        for word in strs:
6            key = ''.join(sorted(word))
7
8            if key not in hashmap:
9                hashmap[key] = []
10            
11            hashmap[key].append(word)
12        return list(hashmap.values())