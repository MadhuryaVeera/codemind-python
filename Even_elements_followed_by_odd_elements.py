n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
for j in l:
    if j%2!=0:
        odd.append(j)
k=even+odd
print(*k)