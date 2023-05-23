n=int(input())
s=0
m=0
a=list(map(int,input().split()))
for i in range(0,n):
    if a[i]%2!=0:
        s=s+a[i]
for i in range(0,n):
  if a[i]%2==0:
      m=m+a[i]
print(abs(s-m))