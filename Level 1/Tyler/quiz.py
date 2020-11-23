# Welcome message (ASCII Art)
def introduction():

    print("\ \ \/\ \ \ \     __   \//\ \      ___     ___     ___ ___       __              ")
    print(" \ \ \ \ \ \ \  /'__`\   \ \ \    /'___\  / __`\ /' __` __`\   /'__`\            ")
    print("  \ \ \_/ \_\ \/\  __/    \_\ \_ /\ \__/ /\ \L\ \/\ \/\ \/\ \ /\  __/            ")
    print("   \ `\___x___/\ \____\   /\____\\ \____\\ \____/\ \_\ \_\ \_\\ \____\           ")
    print("    '\/__//__/  \/____/   \/____/ \/____/ \/___/  \/_/\/_/\/_/ \/____/           ")
   
    print("Hey there, wlcome to Tyler's quiz, today I will be quizing you on the knowledege of disney movies:) ")

# Function for middle of quiz
def middle():
    print(" You've made it this far in the quiz, your doing great. In this half of the quiz, the questions are going to be abit more difficult, you'll have to up your game, goodluck, sorry not sorry ahahahahahha" )

# Function for end of quiz which puts the name and score of questions correct in txt file caled scores.txt
def conclusion(correct, name):
    print("Thankyou for taking part in my quiz, I hope you learnt something about disney movies.")
    print()
    print("===========================================================================================================================")
    f = open("scores.txt", "a+")
    f.write("{} got {} questions correctly.".format(name, correct))

introduction()

# Ask the user for their name and then prints "Welcome [name]"
name=input("Before starting this quiz, what is your name?:")
print("Welcome " + name)

print()
print("==================================================================================================================")

# Correct answers starts at 0 and increases by 1 after every correct answer
correct = 0

# The questions are run the same way for each question. They have a while loop which keeps asking the question until
# the question is answered with one of the choices given, whether correct or incorrect.
# Each question is repeated the same way.
q1_check=True
while(q1_check):

    q1 = input("In what year did the Lion King come out?\nA) 1990.\nB) 1991.\nC) 1994.\nD) 1998.\nEnter your answer here: ")

    if(q1.lower() == "c" or q1.lower()== "1994"):
        print("Correct, you got it right, relax we geddit ")
        correct+=1
        q1_check=False
    elif(q1.lower()=="a" or q1.lower()== "b" or q1.lower()== "d" or q1.lower()=="1990" or q1.lower()=="1991" or q1.lower()=="1998"):
        print("Incorrect, you got it wrong, ahahaha")
        q1_check=False
    else:
        print("You didn't answer with any of the following answers ")
       
    print()
    print("==================================================================================================================")
q2_check=True
while(q2_check):

    q2 = input("In the movie Frozen 1, who is the main character?\nA) Olaf.\nB) Elsa.\nC) Anna.\nD) Kristoff.\nEnter your answer here: ")

    if(q2.lower() == "b" or q2.lower()== "elsa"):
        print("Correct, you got it right, keep it going ;) ")
        correct+=1
        q2_check=False
    elif(q2.lower()=="a" or q2.lower()=="c" or q2.lower()=="d" or q2.lower()=="olaf" or q2.lower()=="anna" or q2.lower()=="kristoff"):
        print("Incorrect")
        q2_check=False
    else:
        print("You didn't answer with any of the following answers ")
       
    print()
    print("===================================================================================================================")

q3_check=True
while(q3_check):
     
    q3 = input("What are the dwarf's names in order, from the movie snow white and the seven dwarfs. ?\nA) Sleepy, Happy, Bashful, Grumpy, Doc, Dopey, Sneezy.\nB) Bashful, Doc, Dopey, Happy, Sleepy, Sneezy, Grumpy.\nC) Grumpy, Happy, Sneezy, Doc, Bashful, Sleepy, Dopey.\nD) Dopey, Sneezy, Bashful, Doc, Happy, Grumpy, Sleepy.\nEnter your answer here: ")
         
    if(q3.lower() == "d" or q3.lower() == "dopey, sneezy, bashful, doc, happy, grumpy, sleepy" ):
        print("Correct, your on fire:) ")
        correct+=1
        q3_check=False
    elif(q3.lower()=="a" or q3.lower()=="b" or q3.lower()=="c"):
        print("Incorrect, ahahahaha, the correct answer was D")
        q3_check=False  
    else:
        print("You didn't answer with any of the given answers ")
           
    print()
    print("===================================================================================================================")
         

q4_check=True
while(q4_check):
   
    q4 = input("Is rudolph the red nosed reindeer male or female. ?\nA) Male.\nB) Female.\nEnter your answer here: ")
   
    if(q4.lower() == "b" or q4.lower() == "female"):
        print("You got it right :) ")
        correct+=1
        q4_check=False
    elif(q4.lower()=="a" or q4.lower()=="male"):
        print("Sorry you got it wrong, hahahaha, research sates that As opposed to females that keep their antlers all winter, and young males that only shed theirs after the Christmas holidays. Therefore, science cannot explain the fiction: all the evidence suggests that Rudolph and its companions are females or young males.")
        q4_check=False
    else:
        print("You did't answer with any of the following answers ")
       
    print()
    print("====================================================================================================================")
   
   
q5_check=True
while(q5_check):

    q5 = input("In the movie peter pan, did Captain Hook have a hook on his left hand or his right hand. ?\nA) His right hand. \nB) His left hand. \nEnter your answer here: ")
   
    if(q5.lower() == "b" or q5.lower() == "left hand"):
        print("Correct, your a pro at this:)")
        correct+=1
        q5_check=False
    elif(q5.lower()=="a" or q5.lower()=="right hand"):
        print("Incorrect, try again next time, hahahahaha")
        q5_check=False
    else:
        print("You didn't answer with any of the following answers ")
       
    print()
    print("======================================================================================================================")

# The middle() function is accessed with an encouraging message.
middle()
print()
print("==============================================================================================================================")

q6_check=True
while(q6_check):
   
    q6 = input("In which city is the Disney movie Ratatouille based. ?\nA)London. \nB)Paris. \nC)Singapore. \nD)New York. \nEnter your asnwer here: ")
   
    if(q6.lower() == "b" or q6.lower() == "paris"):
        print("Wow I didn't except you to get this one, but its correct:)")
        correct+=1
        q6_check=False
    elif(q6.lower() == "a" or q6.lower() == "c" or q6.lower() =="d" or q6.lower() == "london" or q6.lower() == "singapore" or q6.lower() == "new york"):
        print("hahahahaha you got it wrong, the correct answer was Paris")
        q6_check=False
    else:
        print("You didn't answer with any of the given answers")
       
    print()
    print("=====================================================================================================================")
   
   
q7_check=True
while(q7_check):
   
    q7 = input("In the movie Aladdin, What type of animal does Jasmine have for a pet?\nA)Tiger. \nB)Snake. \nC)Cat. \nD)Lizard. \nEnter your answer: ")
   
    if(q7.lower() == "a" or q7.lower == "tiger"):
        print("You got it right, correct:)")
        correct+=1
        q7_check=False
    elif(q7.lower() == "b" or q7.lower() == "c" or q7.lower() == "d" or q7.lower() == "snake" or q7.lower() == "lizard" or q7.lower() == "cat"):
        print("Incorrect hehehe, the correct answer was Tiger")
        q7_check=False
    else:
        print("You didn't answer with any of the following answers")
       
    print()
    print("======================================================================================================================")
   
   
q8_check=True
while(q8_check):

    q8 = input("In the movie Dumbo, what type of animal were Dandy Fat Glasses Preacher and Straw Hat?\nA)Cows. \nB)Mice. \nC)Elephants. \nD)Crows. \nEnter your answer here: ?")
   
    if(q8.lower() == "d" or q8.lower() == "crows"):
        print("Correct, :)")
        correct+=1
        q8_check=False
    elif(q8.lower() == "a" or q8.lower() == "b" or q8.lower() == "c" or q8.lower() == "cows" or q8.lower() == "mice" or q8.lower() == "elephants" or q8.lower == "crows"):
        print("Incorrect, you got this wrong, the correct answer was crows")
        q8_check=False
    else:
        print("You didn't answer with any of the given answers")
       
    print()
    print("========================================================================================================================")
   

q9_check=True
while(q9_check):
   
    q9 = input(" What is the wizard’s name in the movie The Sword in the Stone?\nA)Jospeh. \nB)Blaze. \nC)Merlin. \nD)Warlock \nEnter your answer here: ")
   
    if(q9.lower()=="c" or q9.lower=="merlin"):
        print("Correct:)")
        correct+=1
        q9_check=False
    elif(q9.lower()=="a" or q9.lower()=="b" or q9.lower()=="d" or q9.lower()=="jospeh" or q9.lower()=="blaze" or q9.lower()=="warlock"):
        print("Incorrect aahahahaha, the correct answer was merlin")
        q9_check=False
    else:
        print("You didn't answer with any of the following answers")
       
    print()
    print("========================================================================================================================")
   

q10_check=True
while(q10_check):
   
    q10 = input("Randall Boggs is a villain in which Disney movie?\nA)Monters Inc. \nB)A Bug's Life. \nC)Robin Hood. \nD)Toy Story. \nEnter your answer here: ")
   
    if(q10.lower()=="a" or q10.lower()=="monsters inc"):
        print("Correct:)")
        correct+=1
        q10_check=False
    elif(q10.lower()=="b" or q10.lower()=="c" or q10.lower()=="d" or q10.lower =="a bugs life" or q10.lower()=="bugs life" or q10.lower=="robin hood" or q10.lower()=="toy story"):
        print("Incorrect hahaha, the correct answer was Monsters Inc")
        q10_check=False
    else:
        print("You didn't answer with any of the given answers")
       
    print()
    print("=========================================================================================================================")
   
   
q11_check=True
while(q11_check):

    q11 = input("In the movie Finding Nemo, which country has Nemo been taken to?\nA)Romania. \nB)Austrilia. \nC)United Kingdom. \nD)America. \nEnter your answer here: ")
   
    if(q11.lower()=="b" or q11.lower()=="austrilia"):
        print("Correct:)")
        correct+=1
        q11_check=False
    elif(q11.lower()=="a" or q11.lower()=="c" or q11.lower=="d" or q11.lower()=="romania" or q11.lower()=="united kingdom" or q11.lower()=="america"):
        print("Incorrect hahahaha, the correct answer was Austrilia")
        q11_check=False
    else:
        print("You didn't answer with any of the following answers")
       
    print()
    print("==========================================================================================================================")
   
   
q12_check=True
while(q12_check):
   
    q12 = input("What is the name of Donald Duck’s sister?\nA)Daisy. \nB)Dumbella. \nC)Daphne. \nD)Deborah. \nEnter your answer here: ")
   
    if(q12.lower()=="b" or q12.lower()=="dumbella"):
        print("Correct:)")
        correct+=1
        q12_check=False
    elif(q12.lower()=="a" or q12.lower()=="c" or q12.lower()=="d"or q12.lower()=="daisy" or q12.lower()=="daphne" or q12.lower()=="deborah"):
        print("Incorrect hahaha, the correct answer was Dumbella")
        q12_check=False
    else:
        print("You didn't answer with any of the following answers")
       
    print()
    print("==========================================================================================================================")
   
# The final score and name is then passed to the conclusion() function. The conclusion() function will then save the name and score to the txt file.
conclusion(correct, name)

