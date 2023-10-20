from math import sqrt
def prime(n):
   
    if (n==0 or n==1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
           return False
    return True
t=int(input())

for z in range (t):
    n=int(input())
   
    i,x,y=1,0,0
    r,k=False,False
    if (prime(n)==True):
        print(n)
        
    else:
        while True:
            y=n-i
            x=n+i
            if prime(x)==True:
                r=True
            if prime(y)==True:
                k=True
            i+=1
            if(k==True or r==True):
                break
        if (r==True and k==True):
            print(y)
        elif(r==True and k==False):
            print(x)
        else:
            print(y)
        