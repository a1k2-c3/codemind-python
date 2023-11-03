r,c= map(int,input().split())
mat=[];s=0
for i in range(r):
    inner_list=list(map(int,input().split()))[:c:]
    mat.append(inner_list)
for i in mat:
    for j in i:
        s=s+j
print(s)        