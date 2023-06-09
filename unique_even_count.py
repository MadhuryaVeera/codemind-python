n=int(input())
l=list(map(int,input().split()))
c=0
d=set(l)
for i in d:
    if i%2==0:
        c=c+1
print(c)