n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=0
k=sum(l)
for i in l:
    if i>=a and i<=b:
        d=d+i
print(k-d)