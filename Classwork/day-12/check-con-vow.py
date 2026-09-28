# count the no f vowels and consonants in the given string 
# the string will contain only alphabets
# but it can have both uppercase and lower case

a = input("Enter String :")
vo = 0
cons = 0

for i in range(len(a)):
    if a[i].isalpha():
        if a[i] in "aeiouAEIOU":
            vo += 1
        else:
            cons += 1

print(f"{cons} {vo}")
