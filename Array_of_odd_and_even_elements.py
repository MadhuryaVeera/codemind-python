n=int(input())
l=list(map(int,input().split()))
odd=[]
even=[]
for i in l:
    if i%2!=0:
        odd.append(i)
for j in l:
    if j%2==0:
        even.append(j)
k=odd+even
print(*k)