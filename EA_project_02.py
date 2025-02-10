def conversation():
    print("Welcome to my intervew, this is Elvis student from Gutman Community College")
    print("In this interview I am goin to ask some quiestion about my self until i write 'exit'.")
    
    name = input("Wat is your name? {}". format("Elvis Alejandro"))
    ege = input("how old are you?")
    favorite_show = input("waht is your favorite_show about Elementary? Answer commedy or entretaiment")
    answer = input("about entretaiment?")
    if answer == "about entretaiment" :
        print("Great!! What is your favorite movie?")
        answer = input("harry Potter")
    print(" That's interting to know about you..!") 
       
    programming = input("Do you like programming? {}". format("Answer yes or not"))
    answer = ("yes")
    if answer == "yes":
        print ("That's nice to heard that welcome to IT !!")
    else:
        print ("It was nice to know about you, Elvis Alejandro.")
    
    food = input("What's your favorite food, Elvis?")
    if food == "The Mole, The Mole is traditional Oaxaca's Mexican Food.": 
        print ("ohoo! sounds spyci...")
    else:
        pets = input("Do you have pets? 'Exit' ")
    print ("I look forward to meeting you again and having a more in-depth conversation")
    print ("here we go..!!")

if __name__ == "__main__":
   conversation()