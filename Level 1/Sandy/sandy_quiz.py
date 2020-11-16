
def introduction(name):
    print("================================================================================================")
    print()
    print("888b      88  88888888ba         db            88888888ba   88        88  88           88888888888  ad88888ba")
    print("8888b     88  88      \"8b       d88b           88      \"8b  88        88  88           88          d8\"     \"8b")
    print("88 `8b    88  88      ,8P      d8'`8b          88      ,8P  88        88  88           88          Y8,        ")
    print("88  `8b   88  88aaaaaa8P'     d8'  `8b         88aaaaaa8P'  88        88  88           88aaaaa     `Y8aaaaa,  ")
    print("88   `8b  88  88\"\"\"\"\"\"8b,    d8YaaaaY8b        88\"\"\"\"88\'    88        88  88           88\"\"\"\"\"       `\"\"\"\"\"8b,")
    print("88    `8b 88  88      `8b   d8\"\"\"\"\"\"\"\"8b       88    `8b    88        88  88           88                  `8b")
    print("88     `8888  88      a8P  d8'        `8b      88     `8b   Y8a.    .a8P  88           88          Y8a     a8P ")
    print("88      `888  88888888P\"  d8'          `8b     88      `8b   `\"Y8888Y\"'   88888888888  88888888888  \"Y88888P\"")
    print()
    print("================================================================================================")
    print()
    print(" 10 questions to answer. enjoy and have fun!!")
    print()
    print("Welcome {} to my Quiz".format(name))

 

def highscore(name, score):
    file = open("highscores.txt", "a")
    file.write("{} has a score of {}\n".format(name, score))
    file.close()
name = input("What is your name?\n>>")
introduction(name)
print("================================================================================")
print()
score = 10




while(True):
    q1 = input("what is it called when a player grabs a missed shot?\nA) take away\nB) rebound\nC) hold\nD) steal\n== ")
    
    incorrect = ["a", "c", "d"]
 
    if(q1.lower() == "b"):
        print("Correct")
        score =+ 1
        break
    elif(q1.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("try again")
        print()

while(True):
    q2 = input("why does an offense get two points if the ball is tipped above the rim by a defender?\nA) early blocking foul\nB) scoring block\nC) stoppage\nD) goaltending\n>> ")
    
    incorrect = ["a", "b", "c"]
 

    if(q2.lower() == "d"):
        print("Correct")
        score =+ 1
        break
    elif(q2.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("so close")
        print()
    

while(True):
    q3 = input("each team is allowed to put how many players on the court?\nA) six\nB) 3\nC) five\nD) 7\n== ")
    incorrect = ["a", "b", "d"]
 
    if(q3.lower() == "c"):
        print("Correct")
        score =+ 1
        break
    elif(q3.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("nearly")
        print()
    

while(True):
    q4 = input("are you familiar with how the NBA determines who gets the basketball to start a game?\nA) tip off\nB) coin flip\nC) away team\nD) home team\n>> ")
    incorrect = ["d", "b", "c"]
 
    if(q4.lower() == "a"):
        print("Correct")
        score =+ 1
        break
    elif(q4.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("not quite")
        print()
        
        

while(True):
    q5 = input("do you know which position is typically responsible for orchestrating an offense?\nA) shooting guard \nB) pointing guard\nC) point guard\nD) center\n== ")
    incorrect = ["a", "b", "d"]
 
    if(q5.lower() == "c"):
        print("Correct")
        score =+ 1
        break
    elif(q5.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("my brain is not functioning")
        print()
        
while(True):
    q6 = input("if a player wants to substitute into the game, they must go where?\nA) scorer's table\nB) entrance\nC) substitute line\nD) judges table\n>> ")
    incorrect = ["d", "b", "c"]
 
    if(q6.lower() == "a"):
        print("Correct")
        score =+ 1
        break
    elif(q6.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("almost right")
        print()


while(True):
    q7 = input("the best players can get inside for an easy lay up, which is worth how many points?\nA) twoo points\nB) 2 points\nC) 1 point\nD) onne point\n== ")
    incorrect = ["a", "d", "c"]
 
    if(q7.lower() == "b"):
        print("Correct")
        score =+ 1
        break
    elif(q7.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("try harder")
        print()
    



while(True):
    q8 = input("where does a player go to shoot foul shots?\nA) penalty box\nB) side line\nC) base line\nD) foul line\n>> ")
    incorrect = ["a", "b", "c"]
 
    if(q8.lower() == "d"):
        print("Correct")
        score =+ 1
        break
    elif(q8.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("nevermind repeat")
        print()


while(True):
    q9 = input("what type of defense requires each defender to play a single offensive player one on one?\nA) trap defense\nB) man defense\nC) defense\nD) zone defense\n== ")
    incorrect = ["a", "d", "c"]
 
    if(q9.lower() == "b"):
        print("Correct")
        score =+ 1
        break
    elif(q9.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("again and again")
        print()
print()


while(True):
    q10 = input("What is it called when an offensive player without the ball sets a screen then moves towards the basket?\nA) power screen\nB) screen\nC) pick and roll\nD) hold\n>> ")
    incorrect = ["a", "b", "d"]
 
    if(q10.lower() == "c"):
        print("Correct")
        score =+ 2
        break
    elif(q10.lower() in incorrect):
        print("Incorrect")
        break
    else:
        print("its the last question")
        print()


def conclusion():
    print("yes you finished the quiz. how did you do? thanks for playing the quiz!!")

conclusion()

highscore(name, score)