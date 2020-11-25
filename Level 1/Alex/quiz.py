# created by Alex Vakauta
# 12/11/2020


# this function welcomes the user to the quiz.
def introduction(name):
    print("\nWelcome {} to my Quiz".format(name))

 
# this funtion calulates the users points and adds it to the txt file.
def highscore(name, score):
    file = open("highscores.txt", "a")
    file.write("{} has a score of {}\n".format(name, score))
    file.close()

 
# ask for the users name.
name = input("What is your name?\n>>")
introduction(name)

 
# the score equalls 0 before the quiz asks question.
score = 0

 
# the while loop will repeat if the user doesn't enter any of the correct input.
# this applies for the nexts of couple of question.
while(True):
    q1 = input("What year did cadillac get bulit?\n[1902]\n[1935]\n[1993]\n[1992]\n>>")
    wrong=["1935","1993","1992"]
 
	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
    if(q1.lower() == "1902"):
        print("Correct\n")
        score =+ 1
        break
    elif(q1.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't enter any of the following years.\n")
		
	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q2 = input("What is the fastest car in the world?  \n[(A)Bugatti Veyron Super Sport)]\n[(B)Koenigsegg CCXR Trevita ($4.8M)]\n[(C)W Motors Lykan Hypersport ($3.4M) ]\n[(D)Mansory Vivere Bugatti Veyron ($3.4M) ]\n>>")
    wrong=["b","c","d"]

    if(q2.lower() == "a"):
        print("Correct\n")
        score =+ 1
        break
    elif(q2.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")
	
	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q3 = input("How Often Should I Check My Tire Pressure?\n[(a) every 30 days]\n[(b) every 20 days]\n[(c) every 15 days]\n[(d) every 10 days]\n>>")
    wrong=["every 20 days","every 15 days","every 10 days","b","c","d"]

    if(q3.lower() == "every 30 days" or q3.lower()=="a"):
        print("Correct\n")
        score =+ 1
        break
    elif(q3.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")

	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q4 = input("You should always have a spare of this in your trunk?\n[a) Radio]\n[b) Tire]\n[c) Steering wheel]\n[d) Seatbelt]\n>>")
    wrong=["radio","steering wheel","seatbelt", "a", "c", "d"]

    if(q4.lower() == "tire"):
        print("Correct\n")
        score =+ 1
        break
    elif(q4.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")    

	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q5 = input("which vehicle is the best-selling of all time?\n[a) Ford F-Series]\n[b) Toyota Corolla]\n[c) Chevrolet Corvette]\n[d) GMC Sierra]>>")
    wrong=["ford f-series","gmc sierra","chevrolet corvette", "a","c","d"]

    if(q5.lower() == "toyota corolla"):
        print("Correct\n")
        score =+ 1
        break
    elif(q5.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")  

	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q6 = input("What is the name of the device used to lift a car during a tire change? \na) Lull b) Jack]\n[c) Mike ]\n[d) Tree]\n>>")

    wrong=["lull", "mike", "tree", "c","b","d"]

    if(q6.lower() == "jack" ir q6.lower() == "b"):
        print("Correct\n")
        score =+ 1
        break
    elif(q6.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")

	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q7 = input("Fastest BMW in the world?\n[a)2009 bmw activehybrid ]\n[b) 1994 BMW M5]\n[c) 2011 BMW 640i SE Convertible]\n[d) 1997 BMW M3 Sedan]\n>>")
    wrong = ["1994 BMW M5", "2011 BMW 640i SE Convertible", "1997 BMW M3 Sedan"]
 
    if(q7.lower() == "2009 bmw activehybrid" or q7.lower()=="a"):
        print("Correct\n")
        score =+ 1
        break
    elif(q7.lower() == "b" or q7.lower() == "c" or q7.lower() == "d" or q7.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")

	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q8 = input("Squealing your way to the stop light? That sound usually means you need to replace\n[a) Brakes]\n[b) Tires]\n[c) Windshield]\n[d) Engine]\n>>")
    wrong = ["tires","windshield","engine","b","c","d"]

    if(q8.lower() == "brakes" or q8.lower()=="a"):
        print("Correct\n")
        score =+ 1
        break
    elif(q8.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")

	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q9 = input("Which part of the car is responsible for helping the engine stay cool?\n[a) radiator]\n[b) muffler]\n[c) 1993]\n[d) 1992]\n>>")


    if(q9.lower() == "radiator"):
        print("Correct\n")
        score =+ 1
        break
    elif(q9.lower() == "muffler" or q8.lower() == "20,000 miles" or q8.lower() == "100,000 miles"):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")
  
  	# correct answer will add 1 point.
	# INCORRECT IT WILL GIVE 0 POINT.
	# WITH YOU DIDNT PICK ANY OF THE OPTION IT WILL REPEAT AGAIN.
	# BREAK IT WILL BREAK FROM THE WHILE LOOP.
while(True):
    q10 = input("HINT How often should you get an oil change, on average, to keep your car running smoothly?\n[5,000 miles]\n[3,000 miles]\n[20,000 miles]\n[100,000 miles]\n>>")
    wrong = ["5,000 miles","3,000 miles","20,000 miles","100,000 miles"]

    if(q10.lower() == "5000 miles" or q10.lower() == "5000" or q10.lower() == "5,000 miles" or q10.lower() == "5,000" or q10.lower() == "a"):
        print("Correct\n")
        score =+ 1
        break
    elif(q10.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't one of the options.\n")



highscore(name, score)