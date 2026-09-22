# a = [1, 2, 3]
# index = [1, 0, 2]

# if len(a) != len(index):
#     print("Operation Not possible")
# else:
#     temp = a.copy()  
#     for i in range(len(a)):
#         for j in range(len(index)):
#             if i == j:
#                 a[i] = temp[index[j]]

# print(a)
a = [1, 2, 3]
index = [1, 0, 2, 3]

if len(a) != len(index):
    print("Operation Not possible")
else:
    result = [a[i] for i in index]
    print(result)  