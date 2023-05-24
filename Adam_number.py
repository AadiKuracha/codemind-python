n=int(input())
k=n*n
s=b=0
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
f=s*s 
while(f>0):
    j=f%10
    b=b*10+j
    f=f//10
if b==k:
    print(True)
else:
    print(False)