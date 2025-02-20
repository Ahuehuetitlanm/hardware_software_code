def binary_to_decimal_with_steps(binary_str):
    # Check if the input is a valid binary number
    for digit in binary_str:
        if digit not in ['0', '1']:
            return "Invalid binary number"
    
    # Convert binary to decimal with steps
    decimal = 0
    length = len(binary_str)
    steps = []
    
    for i, digit in enumerate(binary_str):
        power = length - i - 1
        value = int(digit) * (2 ** power)
        steps.append("({digit} * 2^{power})")
        decimal += value
    
    # Display the steps and result
    print(" + ".join(steps))
    print(" + ".join(map(str, [int(digit) * (2 ** (length - i - 1)) for i, digit in enumerate(binary_str)])))
    print("Binary: {binary_str}")
    print("Decimal: {decimal}")
    
    return decimal

def main():
    print("Binary to Decimal Conversion")
    binary_input = input("Enter a valid Binary number (only 0s and 1s): ")
    
    result = binary_to_decimal_with_steps(binary_input)
    if result == "Invalid binary number":
        print(result)

def main():
    print("Choose the following number conversion")
    print("(1) binary to decimal")
    print("(2) decimal to binary")
    print("(3) binary to hexadecimal")
    print("(4) decimal to hexadecimal")
    print("(5) hexadecimal to decimal")
    print("(6) hexadecimal to binary")
    print("(7) octal to decimal")
    print("(8) decimal to octal")
    print("(9) octal to hexadecimal")
    
    selection = input("Selection: ")
    
    if selection == '1':
        print("Converting Binary to Decimal")
        binary_input = input("['0', '1'] are valid numbers\nEnter a valid Binary number: ")
        decimal_value = binary_to_decimal_with_steps(binary_input)
        if decimal_value != "Invalid binary number":
            print("Binary: {binary_input}")
            print("Decimal: {decimal_value}")
        else:
            print(decimal_value)
     
    input("Hit 'Enter' to Continue")
    end_program = input("Type 'yes' to end program: ")
    if end_program.lower() == 'yes':
        return

if __name__ == "__main__":
    main()

