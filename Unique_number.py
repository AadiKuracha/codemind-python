n=int(input())
k=str(n)
c=1
while n!=0:
    r=n%10
    m=k.count(str(r))
    if m!=1:
        c=0
        break
    n=n//10
if c==0:
    print('Not Unique Number')
else:
    print('Unique Number')