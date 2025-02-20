def decimal_to_binary(number):
  result = 0
  if len(number) > 0:
     power = len(str(number)) - 1 # determine gratest power
  for num in str(number):
     result += int(num) * 2 ** power
     power -= 1	#decrease by 1
  return result

def main():
  num = input("Enter Decimal Number: ")
  decimal_num = decimal_to_binary(num)
  print("Decimal {} to Binary: {}". format(num, decimal_num))


if __name__ == "__main__":
		main()
