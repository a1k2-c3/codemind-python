m,n=map(int,input().split())
c=0
for i in range(m,n+1):
    if i%2==0 and i%3==0:
        c+=1
print(c)        