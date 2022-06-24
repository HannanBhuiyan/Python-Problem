num = int(input())
for i in range(1, 6):
    if i % 4 == 1:
       for i in range(1, 4):
           print(num, end="")
       print()
    else:
        for i in range(1, 3):
            print(num, end=" ")
        print()

