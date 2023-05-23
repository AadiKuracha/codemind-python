import math
n=int(input())
s=int(math.sqrt(n))
if n==s*s:
    print(True)
else:
    print(False)