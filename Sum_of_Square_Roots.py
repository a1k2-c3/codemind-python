a,b=map(int,input().split())
s=0
for i in range (a,b+1):
    s=s+(i**(1/2))
print(f'{s:.2f}')    
    