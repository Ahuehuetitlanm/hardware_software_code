def conversation () :
    print ("did you like coding in python? Answer yes or no")
    answer = input ("yes")
    if answer == "yes":
        print ("Thay's good - the United States needs more coders!!")
    else:
        print ("Perhaps you will change your mind ")
    print (" goodby")

def main () : 
    print ("Welcome to my conversation program")
    conversation ()
    print("thanks for chatting with me")
    conversation()

if __name__ == "__main__":
    main()