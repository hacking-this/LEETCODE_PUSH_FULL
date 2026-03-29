1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        mapping = {
5            ')':'(',
6            '}':'{',
7            ']':'['
8        }
9        for i in s:
10            if i in '([{': # checking for opening brackets
11                stack.append(i)
12            else:
13                if not stack or stack[-1]!=mapping[i]: # checking for closing brackets
14                    return False
15                stack.pop()
16        return len(stack)==0
17
18        