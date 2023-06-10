n=int(input())
l=list(map(int,input().split()))
f=[]
w=[]
for i in l:
    d=str(i)
    e=len(d)
    f.append(e)
for j in f:
    d=min(f)
    x=f.count(d)
print(x)
    