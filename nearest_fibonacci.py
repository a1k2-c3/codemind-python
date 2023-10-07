n=int(input());l=[0]
t1=0;t2=1
for i in range (3,100):
    t3=t1+t2
    l.append(t3)
    t1=t2;t2=t3
def incr(n):
    m=[]
    k=n
    d_c=0
    i_c=0
    while n>=0:
        
        if (n) in l:
            a=n
            break
        else:
            d_c+=1
            n=n-1  
    while k>=0:
        if k in l:
            b=k
            break
        else:
            k=k+1
            i_c+=1
    if i_c<d_c:
        m.append(b)
    elif(i_c==d_c):
        m.append(a)
        m.append(b)
    else:
        m.append(a)
    return m
j=incr(n)
print(*j)
        
    