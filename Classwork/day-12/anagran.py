# a = input("Enter first string: ")
# b = input("Enter second string: ")
# c = sorted(a)
# d = sorted(b)
# print(a == b)



# a = input("Enter first string: ")
# b = input("Enter second string: ")
# fre_a = set()
# fre_b = set()
# for i in a:
#     if i not in fre_a:
#         fre_a.add(i)   

# for i in b:
#     if i not in fre_b:
#         fre_b.add(i)
# if fre_a.issubset(fre_b):
#     print(True)
# else:
#     print(False)

a = input("Enter first string: ")
b = input("Enter second string: ")


fre_a = {}
fre_b = {}

for i in a:
    if i not in fre_a:
        fre_a[i] = 1 
    else:
        fre_a[i] += 1 

for i in b:
    if i not in fre_b:
        fre_b[i] = 1
    else:
        fre_b[i] += 1
is_match = True
if fre_b == fre_a:
    print(True)
else:
    print(False)
