def neon(n):
    x=n*n;s=0
    while x>0:
        r=x%10
        s=s+r
        x=x//10
    if s==n:
        print('Neon Number')
    else:
        print('Not Neon Number')
n=int(input()) 
neon(n)