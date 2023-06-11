n=int(input())
l=list(map(int,input().split()))
a=l.count(0)
b=l.count(1)
if (a+b==n):
    print(True)
else:
    print(False)