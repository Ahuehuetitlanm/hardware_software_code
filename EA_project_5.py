def add_numbers():
    print("This program adds two numbers")
    return

def is_valid_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def add_numbers():
    while True:
        first_number = input("Enter first number: ")
        if not is_valid_number(first_number):
            print("Invalid Number, Try again!!!")
            continue
        else:
            print("{first_number} is a good number")
            break

    while True:
        second_number = input("Enter second number: ")
        if not is_valid_number(second_number):
            print("Invalid Number, Try again!!!")
            continue
        else:
            print("{second_number} is a good number")
            break

    print("Let's do some adding!")
    total = int(first_number) + int(second_number)
    print("{} + {} + {} ".format(first_number, second_number, total))

    end_program = input("Type 'yes' to end program: ")
    if end_program.lower() == 'yes':
        print("Good bye!!!")
        print("Come back when you have more numbers:")
        return


if __name__ == "__main__":
    add_numbers()
