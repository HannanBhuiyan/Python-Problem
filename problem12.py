num = int(input())
for i in range(1, 5):
    if i % 2 != 0:
        for j in range(1, 5):
            print(num, end=" ")
        print()
    else:
        for j in range(1, 5):
            print(num, end="")
        print()