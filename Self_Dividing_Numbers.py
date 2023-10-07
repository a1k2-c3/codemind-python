def check(i):
    s=0
    k=i
    c=0
    while i>0:
        rem=i%10
        c+=1
        i=i//10
        if rem==0:
            continue
        if k%rem==0:
            s+=1
        
    if (s==c):
        return True
    else:
        return False
start=int(input())
stop=int(input())
for i in range(start,stop+1):
    if (check(i))==True:
        print(i,end=" ")

        
    
    

            
