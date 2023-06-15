m=int(input())
n=list(map(int,input().split()))
l=list(map(int,input().split()))
for i in range(len(n)):
    o=n[i]+l[i]
    print(o,end=" ")