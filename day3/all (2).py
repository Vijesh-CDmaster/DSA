n, x = map(int, input().split())
a = list(map(int, input().split()))

first = -1
last = -1

for i in range(n):
    if a[i] == x:
        if first == -1:
            first = i
        last = i

print(first, last)