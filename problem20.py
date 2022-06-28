first_number = int(input("Enter First number: "))
second_number = int(input("Enter Second number: "))


def result(first_number, second_number):

    if first_number > second_number:

        return (first_number - second_number) * 2

    # return abs(first_number - second_number)
    return second_number - first_number

print(result(first_number, second_number))
