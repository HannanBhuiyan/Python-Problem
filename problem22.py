number = int(input("Enter First number: "))
def result(number):
    if abs(number - 100) <= 20 or abs(number - 200) <= 20:
        return True
    else:
        return False


print(result(number))