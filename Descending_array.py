n=int(input())
l=list(map(int,input().split()))
d=set(l)
k=sorted(d,reverse=True)
if k==l:
    print('yes')
else:
    print('no')