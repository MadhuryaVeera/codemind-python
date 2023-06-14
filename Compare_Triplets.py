a=list(map(int,input().split()))
b=list(map(int,input().split()))
alice=0
bob=0
for i in range(len(a)):
    for i in range(len(b)):
        if a[i]>b[i]:
            alice=alice+1
        if a[i]<b[i]:
            bob=bob+1
    print(alice,bob,end=' ')
    break