1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        low = 1
4        high = max(piles)
5        ans=0
6        while low<=high:
7            total_time = 0
8            speed = (low+high)//2
9            # for bananas in piles:
10            for i in range(len(piles)):
11                # total_time += math.ceil(bananas/speed)
12                total_time += math.ceil(piles[i]/speed)
13            if total_time<=h:
14                ans = speed
15                high = speed-1
16            else:
17                low = speed+1
18                
19        return ans
20