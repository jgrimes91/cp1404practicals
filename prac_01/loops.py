for i in range (1, 21, 2):
    print(i, end=" ")
print()

for i in range (0, 100, 10):
    print(i, end=" ")
print()

for i in range (20, 0, -1):
    print(i, end=" ")
print()

stars = int(input("Enter number of stars: "))
for i in range (stars):
    n = i + 1
    print("*" * n)