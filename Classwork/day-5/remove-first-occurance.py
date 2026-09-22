# a = list(map(int, input().split()))
# tr = int(input())

# if tr in a:
#     a.remove(tr)
# else:
#     print("Invalid Number")

# print(a)

a = list(map(int, input().split()))
tr = int(input())

pos = -1

for i in range(len(a)):
    if a[i] == tr:
        pos = i
        break

for i in range(len(a)):
    if i != pos:
        print(a[i], end=" ")