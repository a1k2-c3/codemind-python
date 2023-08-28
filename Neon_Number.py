n=int(input())
s=n*n
x=0
while s>0:
    rem=s%10
    x=x+rem
    s=s//10
if x==n:
    print('Neon Number')
else:
    print('Not Neon Number')