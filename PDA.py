n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print('PERFECT')
elif s<n:
    print('DEFICIENT')
else:
    print('ABUNDANT')