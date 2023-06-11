n=int(input())
l=list(map(int,input().split()))
a,b=0,0
for i in range(0,n//2):
    a+=l[i]
for j in range(n//2,n):
    b+=l[j]
print(a)
print(b)
    