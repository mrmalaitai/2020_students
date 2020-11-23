# Jared Huni
# Quiz about General Knowledge

# Welcome function which prints a nice welcome message
def welcome():
    print(" __       __  ________  __        ______    ______   __       __  ______  __    __   ______  ")
    print("|  \  _  |  \|        \|  \      /      \  /      \ |  \     /  \|      \|  \  |  \ /      \ ")
    print("| $$ / \ | $$| $$$$$$$$| $$     |  $$$$$$\|  $$$$$$\| $$\   /  $$ \$$$$$$| $$\ | $$|  $$$$$$\ ")
    print("| $$/  $\| $$| $$__    | $$     | $$   \$$| $$  | $$| $$$\ /  $$$  | $$  | $$$\| $$| $$ __\$$")
    print("| $$  $$$\ $$| $$  \   | $$     | $$      | $$  | $$| $$$$\  $$$$  | $$  | $$$$\ $$| $$|    \ ")
    print("| $$ $$\$$\$$| $$$$$   | $$     | $$   __ | $$  | $$| $$\$$ $$ $$  | $$  | $$\$$ $$| $$ \$$$$")
    print("| $$$$  \$$$$| $$_____ | $$_____| $$__/  \| $$__/ $$| $$ \$$$| $$ _| $$_ | $$ \$$$$| $$__| $$")
    print("| $$$    \$$$| $$     \| $$     \\$$    $$ \$$    $$| $$  \$ | $$|   $$ \| $$  \$$$ \$$    $$")
    print(" \$$      \$$ \$$$$$$$$ \$$$$$$$$ \$$$$$$   \$$$$$$  \$$      \$$ \$$$$$$ \$$   \$$  \$$$$$$")

    print()
    print("========================================================================================================")

# Welcomes user with their name and prints to out
def introduction(name):
    print("Welcome {} to my quiz".format(name))

# Prints highscore and name to txt file
def highscore(name, score):
    # Opens and writes name and score to a txt file
    file =open("highscore.txt", "a")
    file.write("{} has a score of {}\n".format(name, score))
    file.close()

# Intiating score = 0
score=0

# Access welcome message
welcome()

# Asks the user for their name
name=input("What is your name?\n>>" ) 
introduction(name)

print()
print("=======================================================================================================")



# First quetion in a while loop. If user response is not one of the answers, the while loop will loop again.
# Each question is repeated in the same way
while(True): 
    print("\nWho is the oldest Kardashian? \nA Khole Kardashian\nB Kim Kardashian \nC Kourtney Kardashian\nD Rob Kardashian ")
    q1=input(">>")
    # List variable of options for user to choose from
    abc = ["a","b","c","d","Khole Kardashian","Kim Kardashian","Kourtney Kardashian","Rob Kardashian"]
    if(q1 not in abc):

        print("YOU FOOL YOU DIDN'T PICK AN OPTION")
        print("=======================================================================================================")
    elif(q1.lower() == "c" or q1 == "Kourtney Kardashian"):
        score+=1
        print("correct")
        print("=======================================================================================================")
        break
        
    elif(q1.lower() == "b" or q1.lower() == "a" or q1.lower() == "c" or q1.lower() == "d" or q1.lower() == " Kim Kardashian" or q1 == " Khole Kardashian" or q1 == "Rob Kardashian"):
        print("Incorrect")
        print("=======================================================================================================")
        break

# As above, the second question is similar to the first question with if-and-else statements.s
while(True):
    print("\nWhen was Albert Einstein born? \nA 1856 \nB 1882 \nC 1792 \nD 1879")
    q2=input(">>")
    abc = ["a","b","c","d","1856","1882","1792","1879"]
    if(q2 not in abc):
        
        print("GRONK YOU DID IT AGAIN") 
        print("=======================================================================================================")
    elif(q2.lower() == "d" or q2 == "1882"):
        score+=1
        print("correct")
        break
    elif(q2.lower() == "a" or q2.lower() == "b" or q2.lower() == "c" or q2.lower() == "d" or q2.lower() == "1856" or q2 == "1882" or q2 == "1792"):
        print("HALAAAAAAAAA FOOLL")
        print("=======================================================================================================")
        break

print("====================================================================================================")
 
 
#def q3():
while(True):
    print("\nHow many rings does Michael Jordan have? \nA Six\nB Five\nC Seven\nD Four ")
    q3=input(">>")
    abc= ["a","b","c","d","Six","Five","Seven","Four"]
    if(q3 not in abc):
    
        print("NO OPTIONS SELECTED")
        print("=======================================================================================================")
    elif(q3.lower() == "a" or q3.lower() == "six"):
        print("YESSIRR FOOL")
        score+=1
        print("=======================================================================================================")
        break
    elif(q3.lower() == "a" or q3.lower() == "b" or q3.lower() == "c" or q3.lower() == "d" or q3.lower() == "Six" or q3 == "Five" or q3 == "Seven" or q3 == "Four"):
        print("AYYY YOU ACTUALLY THOUGHT GRONK")
        print("=======================================================================================================")
        break 
        
#def q4():
while(True):
    print("\nWhen did Usher's song BURN get released? \nA 2003\nB 2001\nC 2006\nD 2004 ")
    q4=input(">>")
    abc= ["a", "b", "c", "d", "2003", "2001", "2006", "2004"]
    if(q4 not in abc):
    
        print("HALA OPTIONS SELECTED")
        print("=======================================================================================================")
    elif(q4.lower() == "d" or q4 == "2004"):
        score+=1
        print("HOW DID YOU KNOW BOT")
        print("=======================================================================================================")
        break
    elif(q4.lower() == "a" or q4.lower() == "b" or q4.lower() == "c" or q4.lower() == "d" or q4.lower() == "2003" or q4 == "2001" or q4 == "2006" or q4 == "2004"):
        print("NOW YOU HAVE TO LISTEN TO MY SONG, BECAUSE IT'S UNFORTUNATE THAT YOU ARE WRONG")
        print("=======================================================================================================")
        break
        
#def q5():
while(True):
    print("\nWhat is the current world record time for the 100m? \nA 9.58\nB 9.31\nC 10.01\nD 10.26 ")
    q5=input(">>")
    abc= ["a","b","c","d", "9.58", "9.31", "10.01", "10.26" ]
    if(q5 not in abc):
    
        print(" WHAT IS WRONG WITH YOUR BRAIN, CHOOSE AN OPTION")
        print("=======================================================================================================")
    elif(q5.lower() == "a" or q5.lower() == "9.58"):  
        score+=1
        print("STOP GUESSING YAH GRONNK, NAH YEAH YOUR RIGHT")
        print("=======================================================================================================")
        break
    elif(q5.lower() == "a" or q5.lower() == "b" or q5.lower() == "c" or q5.lower == "d" or q5.lower == "9.58" or q5 == "9.31" or q5 == "10.01" or q5 == "10.26" ):
        print(" SHAME YAH BOT YOUR WRONG")
        print("=======================================================================================================")
        break
        
#def q6():
while(True):
    print("\nWhich celebrity has the most followers on twitter? \nA donald trump\nB beyonce\nC barrack obama\nD chris brown")
    q6=input(">>")
    abc= ["a", "b", "c", "d", "donald trump", "beyonce", "barrack obama", "chris brown" ]
    if(q5 not in abc):
    
        print(" SELECT AN OPTION FOOL")
        print("=======================================================================================================")
    elif(q6.lower() == "c" or q6.lower() == "barrack obama"):
        score+=1
        print(" HAHAHA YOU GOT IT RIGHT")
        print("=======================================================================================================")
        break
    elif(q6.lower() == "a" or q6.lower() == "b" or q6.lower() == "c" or q6.lower() == "d" or q6.lower() == "donald trump" or q6 == "beyonce" or q6 == "barrack obama" or q6 == "chris brown" ):
        print(" HAHAHAHAHAHA YOU ACTUALLY THOUGHT YOU BOT")
        print("=======================================================================================================")
        break
        
#def q7():
while(True):
    print("\nWhen is Jared's birthday? \nA 25.12.04\nB 25.06.04\nC 05.03.05\nD 13.11.12")
    q7=input(">>")
    abc= ["a", "b", "c", "d", "25.12.04", "25.06.04", "05.03.04", "13.11.12" ]
    if(q7 not in abc):
    
        print(" CHOOSE A OPTION DORY")
        print("=======================================================================================================")
    elif(q7.lower() == "a" or q7.lower() == "25.12.04"):
        score+=1
        print(" LUCKKYY GUESS BOTT")
        print("=======================================================================================================")
        break
    elif(q7.lower() == "a" or q7.lower() == "b" or q7.lower() == "c" or q7.lower() == "d" or q7.lower() == "25.12.04" or q7.lower() == "25.06.04" or q7.lower() == "05.03.04" or q7.lower() == "13.11.12"):
        print(" YOUU AREE A FAKEE FRIENDD")
        print("=======================================================================================================")
        break

#def q8():
while(True):
    print("\nWho was the first superman actor? \nA clark kent\nB george reeves\nC bruce wayne\nD tom hanks")
    q8=input(">>")
    abc= ["a", "b", "c", "d", "clark kent", "geogre reeves", "bruce wayne", "tom hanks" ]
    if(q8 not in abc):
    
        print(" WHAT AREEE YOUU DOINGGG")
        print("=======================================================================================================")
    elif(q8.lower() == "b" or q8.lower() == " george reeves"):
        score+=1
        print(" FARHH MEANESSTT FLUKKEEE")
        print("=======================================================================================================")
        break
    elif(q8.lower() == "a" or q8.lower() == "b" or q8.lower() == "c" or q8.lower() == "d" or q8.lower() == "clark kent" or q8.lower() == "geogre reeves" or q8.lower() == "bruce wayne" or q8.lower() == "tom hanks" ):
        print(" HAHAHA YOUR THE BIGGESTT GRONNKK")
        print("=======================================================================================================")
        break 
        
#def q9():
while(True): 
    print("\nHow old is KSI? \nA 26\nB 28\nC 29\nD 27")
    q9=input(">>")
    abc= [ "a", "b", "c", "d", "26", "28", "29", "27" ]
    if(q9 not in abc):
        print(" GRONNKKK CHOOSSEE ANNN OPTIIOONNN")
        print("=======================================================================================================")
    elif(q9.lower() == "a" or q9.lower() == "26"):
        score+=1
        print(" YESSSSIRRRRR GRRRRROOONNNNKKKKKKKK")
        print("=======================================================================================================")
        break
    elif(q9.lower() == "a" or q9.lower() == "b" or q9.lower() == "c" or q9.lower() == "d" or q9.lower() == "26" or q9.lower() == "28" or q9.lower() == "29" or q9.lower() == "27" ):
        print(" SHAMMEEEE YOUUUU BOTTTTTT")
        print("=======================================================================================================")
        break
        
#def q10():
while(True):
    print("\nWhen did bruce lee die \nA 1956\nB 1978\nC 1966\nD 1973 ")
    q10=input(">>")
    abc=[ "a", "b", "c", "d", "1956", "1978", "1966", "1973" ]
    if(q10  not in abc):
    
        print(" CHOOSSSEEE ANNN OPPTTTIIIOOOONNNN BOOTTTTTTT")
        print("=======================================================================================================")
    elif(q10.lower() == "d" or q10.lower() == "1973"):
        score+=1
        print(" ULTTTRRAAA LUCCKKKYYY GUEESSSS")
        print("=======================================================================================================")
        break
    elif(q10.lower() == "a" or q10.lower() == "b" or q10.lower() == "c" or q10.lower() == "d" or q10.lower() == "1956" or q10.lower() == "1978" or q10.lower() == "1966" or q10.lower() == "1973"):
        print(" WHATT HAPPEEENNEEDDD DRRIIFFFTTEERRRR")
        print("=======================================================================================================")
        break 

print("{}, you got {} questions correct out of 10.\n".format(name, score))

# Access the highscore function and adds user's name and score
highscore(name, score)