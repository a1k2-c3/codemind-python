a,b,x,y=map(int,input().split())
s=0
for i in range (a,b+1):
    if i%x==0 and i%y!=0:
        s=s+i
print(s)        