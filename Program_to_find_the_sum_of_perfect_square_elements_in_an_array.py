import math
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    k=int(math.sqrt(i))
    if k*k==i:
        s=s+i
print(s)