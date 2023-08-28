n=int(input())
r=0
while n>0:
    e=n%10
    r=(r*10)+e
    n=n//10
print(r)    