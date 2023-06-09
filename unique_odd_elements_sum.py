n=int(input())
l=list(map(int,input().split()))
c=0
d=set(l)
for i in d:
    if i%2!=0 and i!=0:
        c=c+i
print(c)