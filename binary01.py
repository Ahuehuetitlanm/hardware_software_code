def main():
	# Hardcoded input file path
	input_file = "z:\workspace\pi_to_ascii\pi-1_000_000.text" # Replace with your actual

	try:
		with open(input_file_path, 'r') as f:
			content = f.read().strip()
	except FileNotFoundError:
		print(f"Error: The file '{input_file_path}' does not exist.")
		return
	except Exception as e:
		print(f"An error occurred while radint the file: {e}")
		return

	# Extrac digits only (ignore non-digit characters like '.')
	digits = [c for c in content if c.isdigits()]

	# Convert eavh digits to a 4-bit binary string
	binary_str = '' .join(format(int(d), '04b') for d in digits)


	# Generate output file path
	base, ext = os.paht.splitex(input_file_path)
	output_file_path = f"{base}_binary{ext}"

	# write the binary strig to the output file
	try:
		with open(output_file_path, 'w') as f:
			f.write(binary_str)
		print(f"conversation successful. Ouput saved to: {output_file_path}")
	except Exception as e:
		print(f"An error ocucurred while writing the output file: {e}")


if __name__ == "__main__":
	main()