def conversation():
    print("Hellow, I would like to get to know a llitle about you, and I want to know how much you know about soccer.")
    print("Please answer a few brief questions about soccer")

    name = input("Wat is your name?")
    ege = input("how old are you?")
    soccer = input("Do you like Futbol? Answer yes or not")
    answer = input("yes")
    if answer == "yes" :
        print ("I like that answer,let see how much you know")

    best_player = input("who is the best soccer player? Answer Messi or Cristiano R?")
    if answer == "Messi":
        print ("A lot of people thinks Cristiano ronaldo is better than Messi.!!")
    else:
        print ("It was nice to know about you, Elvis Alejandro.")
    print ("I know that you are a athletic person")
    print ("I look forward to meeting you again and having a more in-depth conversation")
    print ("here we go..!!")

if __name__ == "__main__":
   conversation()