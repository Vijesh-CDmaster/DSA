# a=input("Enter String :")
# b=[]
# for i in range(len(a)):
#     b.append(a[-1-i])
# b="".join(b)
# if b == a:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


a = input("Enter String: ")

is_palindrome = True
left = 0
right = len(a) - 1

while left < right:
    if a[left] != a[right]:
        is_palindrome = False
        break   
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
