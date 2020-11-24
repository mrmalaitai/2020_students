import tkinter as tk
from os import walk
"""
def display_students(students):
    display = tk.Toplevel(root)
    
    results = tk.Listbox(display)
    for x in students:
        adding_student = "{} {}".format(students[x], x)
        results.insert(0, adding_student)
    
    results.grid(row = 0, column = 0)
"""
def display_clubs(clubs):
    display = tk.Toplevel(root)
    display.title("Club Points")
    display.iconbitmap("award.ico")
    
    #Turn dictory into list
    points = [ [k,v] for k, v in clubs.items() ]
    
    #Order List
    points.sort(key = lambda x: x[1])
    
    #Display list
    points_listbox = tk.Listbox(display, width = 39, height = 65, font = ("Calibri", 9))
    
    #Adds each team to the listbox "points_listbox"
    for x in points:
    
        if(x[[0][0]] == ""):
            continue
            
        adding_student = "{}".format(x)
        points_listbox.insert(0, adding_student)
           
    points_listbox.grid(row = 0, column = 0)
    print(points)


def calculate_scores(current_year, final_races):
    clubs = {}
    
    for final in final_races:
        current_race = open("{}/{}".format(current_year, final),"r")
        
        
        for club in current_race:
            points = club.strip().split(",")
            
            score = 0
            
            if(points[0] == "1"):
                score = 8
            elif(points[0] == "2"):
                score = 7
            elif(points[0] == "3"):
                score = 6
            elif(points[0] == "4"):
                score = 5
            elif(points[0] == "5"):
                score = 4
            elif(points[0] == "6"):
                score = 3
            elif(points[0] == "7"):
                score = 2
            else:
                score = 1
                
            if(points[5] not in clubs):
                clubs[points[5]] = score
            else:
                clubs[points[5]] = clubs.get(points[5]) + score
               
            
        current_race.close()
    

#    for x in clubs:
 #       print (x, clubs[x])
  #      
   #     for club in current_year:
    #        club = club.strip().split(",")
     #       if(club[1] not in clubs):
      #          students[club[1]] = int(club[5])
       #     else:
        #        score = club.get(club[1]) + int(club[5])
         #       club[club[1]] = score
           
        #current_year.close()
    #display_club(clubs)

            # Converting ito dictionary list
    display_clubs(clubs)

def display_files():
    finals = []
    current_year = final_chosen.get()
    
    for root, dirs, files in walk("{}".format(current_year)):
        finals.extend(files)
        break
    #print(races)
    
    final_races = []
    
    FINAL_NAMES = ["Final"]
    
    for final in finals:
        if("Final" in final):
            final_races.append(final)
    #print(final_races)
    calculate_scores(current_year, final_races)
	
"""
	files = []
	finals = []
	for root, dirs, file in walk("{}".format(final_chosen.get())):
		files.extend(file)
		print(files)
		break
	for file in files:
		if "Final" in file:
			finals.append(file)
	print(finals)
"""
years = []

for root, dirs, files in walk("."):
	years.extend(dirs)
	break

BG_COLOUR="#bb0000"
FG_COLOUR="white"
root = tk.Tk()

root.title("Waka Ama Sprint Nationals")
root.configure(bg=BG_COLOUR)
root.iconbitmap("award.ico")

#By: inipagi
#https://icon-icons.com/icon/Trophy-winner-award/82485

title = tk.Label(root, text = "Waka Ama Sprint Nationals race results and", font = ("Times New Roman",[14]), bg=BG_COLOUR, fg=FG_COLOUR)
title.grid(row = 0, column = 0, columnspan = 3)

title_ = tk.Label(root, text = "award scoring for the competition", font = ("Times New Roman",[14]), bg=BG_COLOUR, fg=FG_COLOUR)
title_.grid(row = 1, column = 0, columnspan = 3)

final_chosen = tk.StringVar()
final_chosen.set("Choose Year")

final_options = tk.OptionMenu(root, final_chosen, *years)
final_options.grid(row = 2, column = 1)

button = tk.Button(root, text = "Display files", command = display_files)
button.grid(row = 4, column = 1)

root.mainloop() 