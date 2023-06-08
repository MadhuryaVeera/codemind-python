n=int(input())
l=list(map(int,input().split()))
c=0
d=set(l)
for i in d:
    c+=i
print(c)