n=int(input())
a=0
x=0
for i in range(1,n+1):
    a=a+i
    s=a**2
for u in range(1,n+1):
    x=x+(u*u)
print(abs(s-x))    