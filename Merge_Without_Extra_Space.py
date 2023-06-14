n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    c=list(set(map(int,input().split())))
    d=list(set(map(int,input().split())))
    k=c+d
    g=sorted(k)
    print(*g)