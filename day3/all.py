import math

n = int(input())
a = list(map(int, input().split()))

print("Scores:")

for i in range(n):
    print(a[i], end=" ")
    if (i + 1) % 4 == 0:
        print()

total = 0
low = a[0]
high = a[0]

for i in range(n):
    total = total + a[i]

    if a[i] < low:
        low = a[i]

    if a[i] > high:
        high = a[i]

avg = total / n

print()
print("Average: {:.2f}".format(avg))
print("Lowest Score:", low)
print("Highest Score:", high)

# 3. Deviation and SD
square = 0

print()
print("Score  Deviation")

for i in range(n):
    deviation = a[i] - avg
    print(a[i], f"   {deviation:.2f}")

    square = square + deviation * deviation

sd = math.sqrt(square / n)

print()
print(f"Standard Deviation: {sd:.2f} ")

# 4. Count within one SD
count = 0

for i in range(n):
    if avg - sd <= a[i] <= avg + sd:
        count = count + 1

print()
print("Scores within one standard deviation:", count)