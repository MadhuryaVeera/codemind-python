n=int(input())
l=list(map(int,input().split()))
N=[]
for i in l:
    if l.count(i)>=n/2:
        N.append(i)
s=set(N)
for j in s:
    print(j)