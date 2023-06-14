n=int(input())
l=list(map(int,input().split()))
k=[]
k.extend(l[n//2:][::-1])
k.extend(l[:n//2])
for i in k:
    print(i,end=' ')