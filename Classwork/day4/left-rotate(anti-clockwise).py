a=list(map(int,input().split()))
n=2
for i in range(n):
    x=a.pop(0)
    a.append(x)
print(a)