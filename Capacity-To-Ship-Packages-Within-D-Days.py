1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        low = max(weights)
4        high = sum(weights)
5        ans = high
6        while low<=high:
7            mid = (low+high)//2
8            days_used = 1
9            total_load = 0
10            for curr_weight in weights:
11                if curr_weight+total_load>mid:
12                    total_load = curr_weight
13                    days_used+=1
14                else:
15                    total_load+=curr_weight
16            if days_used<=days:
17                ans = mid
18                high = mid-1
19            else:
20                low = mid+1
21        return ans
22
23        