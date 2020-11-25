# Created by Trey Wharewaka

# this function called introduction welcomes the user
def introduction(name):
    print("Welcome {} to my Quiz\n".format(name))

# this function called highscore tells the user the points at the end of the game
def highscore(name, score):
    file = open("highscores.txt", "a+")
    file.write("{} has a score of {} out of 10 questions.\n".format(name, score))
    file.close()

# this function called name is where you put your name 
name = input("What is your name?\n>>")
introduction(name)

# the scores equals to 0 before it asks qeutions
score = 0

# input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points 
while(True):
    q1 = input("What year was the supra mk4 made?\n1993\n1994\n1996\n1997\n>>")
    wrong = ["1994", "1996", "1997"]

    if(q1.lower() == "1993"):
        print("Correct\n")
        score += 1
        break
    elif(q1.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 1\n".format(score))
# input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points
while(True):
    q2 = input("What does a s15 belong to?\na) Holden\nb) Toyota\nc) Nissan\nd) Subaru\n>>")
    wrong = ["holden", "toyota", "subaru", "a", "b", "d"]

    if(q2.lower() == "nissan\n" or q2.lower() == "c"):
        print("Correct")
        score += 1
        break
    elif(q2.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 2\n".format(score))
        # input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points
while(True):
    q3 = input("What does a supra belong to?\na) Toyota\nb) Holden\nc) Mitsubishi\nd) Ford\n>>")
    wrong = ["holden", "mitsubishi", "ford", "b", "c", "d"]

    if(q3.lower() == "toyota" or q3.lower()=="a"):
        print("Correct\n")
        score += 1
        break
    elif(q3.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 3\n".format(score))
 # input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points       
while(True):
    q4 = input("What year was the supra mk4 made?\n1993\n1994\n1995\n1996\n>>")
    wrong = ["1993", "1994", "1997"]

    if(q4.lower() == "1996"):
        print("Correct\n")
        score += 1
        break
    elif(q4.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 4\n".format(score))
 # input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points       
while(True):
    q5 = input("when was the nissan r34 built?\n1882\n1992\n1998\n1999\n>>")
    wrong = ["1992", "1999", "1882"]

    if(q5.lower() == "1998"):
        print("Correct\n")
        score += 1
        break
    elif(q5.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 5\n".format(score))
# input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points        
while(True):
    q6 = input("What year did the nissan gtr come out?\n1756\n1820\n1969\n2000\n>>")
    wrong = ["1820", "1756", "2000"]

    if(q6.lower() == "1969"):
        print("Correct\n")
        score += 1
        break
    elif(q6.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 6\n".format(score))
# input: tells us the questions
# wrong:  
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points   
while(True):
    q7 = input("what type of egine does a ford falcon have?\na) xr6\nb) v6\nc) ss\nd) v8\n>>")
    wrong = ["v6", "ss", "v8", "b", "c", "d"]

    if(q7.lower() == "xr6" or q7.lower()=="a"):
        print("Correct\n")
        score += 1
        break
    elif(q7.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 7\n".format(score))
 # input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points       
while(True):
    q8 = input("when was the first acura nsx made?\n1756\n1820\n1990\n2000\n>>")
    wrong = ["1820", "1756", "2000"]

    if(q8.lower() == "1990"):
        print("Correct\n")
        score += 1
        break
    elif(q8.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 8\n".format(score))
# input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points
while(True):
    q9 = input("when was the cadillac firts made?\n1930\n1857\n2004\n1902\n>>")
    wrong = ["1930", "1857", "2004"]

    if(q9.lower() == "1902"):
        print("Correct\n")
        score += 1
        break
    elif(q9.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 9\n".format(score))
# # input: tells us the questions
# wrong: this tells us the years 
# if: tells us the right answeer
# correct answer will give you one point
# print: you didnt choose a qeustions
# if inccorect it gives 0 points
while(True):
    q10 = input("when did they first start making harley?\n1837\n1937\n1903\n1999\n>>")
    wrong = ["1837", "1937", "1999"]
    if(q10.lower() == "1903"):
        print("Correct\n")
        score += 1
        break
    elif(q10.lower() in wrong):
        print("Incorrect\n")
        break
    else:
        print("You didn't choose one of the options.\n")
print("Questions correct: {} out of 10\n".format(score))

print("Congrats {}, you scored {} out of 10 questions. Thanks for playing.".format(name, score))
highscore(name, score)








