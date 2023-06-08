n=int(input())
l=list(map(int,input().split()))
c,d=0,0
for i in l:
    if i%2==0:
        c=c+i
    else:
        d=d+i
print(abs(c-d))