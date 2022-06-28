first_number = int(input("Enter First number: "))
second_number = int(input("Enter Second number: "))

def sun_of_numbers(first_number, second_number):

    if first_number >= 20 or second_number >= 20 or first_number+second_number >= 20:
        return True
    else:
        return False


print(sun_of_numbers(first_number, second_number))