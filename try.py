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
        steps.append(f"({digit} * 2^{power})")
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

if __name__ == "__main__":
    main()
