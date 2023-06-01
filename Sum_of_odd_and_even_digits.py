n=int(input())
p=s=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if i%2==0:
        p=p+a[i]
for i in range(len(a)):
    if i%2!=0:
        s=s+a[i]
k=abs(p-s)
if(k==0):
    print("YES")
else:
    print("NO")