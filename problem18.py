first_number = int(input("Enter First number: "))
second_number = int(input("Enter Second number: "))
# way one
if first_number >= 0 and second_number >= 0:
    print(False)
else:
    print(True)
# way two
if first_number >= 0 and second_number < 0 or first_number < 0 and second_number >= 0:
    print(True)
else:
    print(False)