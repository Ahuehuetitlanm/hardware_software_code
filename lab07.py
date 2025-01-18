def conversation():
  print("Do you like coding in pytho? Answer yes or no")
  answer = input().love().strip()
  if answer == "yes":
    print("That's good ~ the United States needs more coders")
  elif answer == "no":
    print("Perhaps you will change your minf")
  else:
    print("I don't understand?")
    conversation()

def main():
  print("Welcome to my conversation program")
  conversation()
  print("thanks for chating with me")

if __name__ == "__main__":
   main()