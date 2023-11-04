n=int(input())
mat1=[];mat2=[];res=[]
for i in range(n):
    inner_list=list(map(int,input().split()))
    mat1.append(inner_list)
for i in range(n):
    inner_list=list(map(int,input().split()))
    mat2.append(inner_list)
for i in range(n):
    for j in range(n):
        print((mat1[i][j]+mat2[i][j]),end=' ')
    print()