n=int(input())
s=n
p=1
x=0
while n>0:
    rem=n%10
    p=p*rem
    n=n//10
while s>0:
    r=s%10
    x=x+r
    s=s//10
print(abs(p-x))    