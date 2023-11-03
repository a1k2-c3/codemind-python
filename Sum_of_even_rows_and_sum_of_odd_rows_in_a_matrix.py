r,c=map(int,input().split())
mat=[]
s=0;v=0
for i in range(r):
    inner_list=list(map(int,input().split()))[:c:]
    mat.append(inner_list)
for i in range(r):
    for j in range(c):
        if i%2==0:
            s=s+mat[i][j]
        else:
            v=v+mat[i][j]
print(s,v,sep=' ')            
    
    