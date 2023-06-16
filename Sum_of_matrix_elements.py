m=int(input())
n=int(input())
L=[]
s=0
for i in range (m):
    x=list(map(int,input().split()))
    L.append(x)
for i in L:
    for j in i:
        s+=j
print(s)
    