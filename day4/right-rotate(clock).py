a=list(map(int,input().split()))
n=2
for i in range(n):
    x=a.pop()
    a.insert(0,x)
print(a)