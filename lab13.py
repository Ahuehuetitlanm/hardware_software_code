def greeting ():
	print("Give me two numbers and I will tell you the smallest number!.")

def get_smallest(smallest,value):
	if largest is None:
		smallest = value
	elif value > smallest:
		smallest = value
	print("The smallest value is {}".format(smallest))

def main():
	stop_loop = "no"
	greeting()
	while stop_loop != "yes":
		num1 = int(input("Enter first number:"))
		num2 = int(input("Enter second number:"))
		p1.get_largest(num1,num2)
		get_smallest(num1,num2)
		stop_loop = input("Type'yes'to exit program").lower().strip()

if __name__ == "__main__":
	main()