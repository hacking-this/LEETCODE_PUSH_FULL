1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        low = 1
4        high = num
5        while low<=high:
6            mid = (low+high)//2
7            square = mid * mid
8            if square == num:
9                return True
10            elif square>num:
11                high = mid-1
12            else:
13                low = mid+1
14        return False
15        