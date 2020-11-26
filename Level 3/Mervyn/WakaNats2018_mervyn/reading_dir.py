import tkinter as tk # Used for creating the GUI
from os import walk # Used to read files and folders

# The display_clubs function displays the clubs in order from most points to least points in a second GUI window
def display_clubs(clubs):
    display = tk.Toplevel(root)
    display.title("Club Points")
    display.iconbitmap("icon.ico")
    
    #Turn dictory into list to make it easier to sort in order
    points = [ [k,v] for k, v in clubs.items() ]
    
    #Order List from most points to least points
    points.sort(key = lambda x: x[1])
    
    #Displays the list of teams
    points_listbox = tk.Listbox(display, width = 39, height = 65, font = ("Calibri", 9))
    
    #Adds each team to the listbox "points_listbox"
    for x in points:
    
        if(x[[0][0]] == ""):
            continue
            
        adding_student = "{}".format(x)
        points_listbox.insert(0, adding_student)
           
    points_listbox.grid(row = 0, column = 0)
    print(points)

# calculate_scores function calculates how many points that team has scored depending on their position in the .lif file
def calculate_scores(current_year, final_races):
    clubs = {}
    
    for final in final_races:
        current_race = open("{}/{}".format(current_year, final),"r")
        
        
        for club in current_race:
            points = club.strip().split(",")
            
            score = 0
            
            # First place gets 8 points, Second gets 7 points and so on.
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
    
    display_clubs(clubs)

# The display_files function loops through and finds all the files in the chosen directory
def display_files():
    finals = []
    current_year = final_chosen.get()
    
    # Loops through the folders and files while adding the necessary files from the necessary folder
    for root, dirs, files in walk("{}".format(current_year)):
        finals.extend(files)
        break
    
    final_races = []
    
    # Loops through the files and grabs files with "Final" in it
    for final in finals:
        if("Final" in final):
            final_races.append(final)
    calculate_scores(current_year, final_races)
	
years = []

for root, dirs, files in walk("."):
    years.extend(dirs)
    break

# Constants for colours
BG_COLOUR="#bb0000"
FG_COLOUR="white"

root = tk.Tk()

# Adding a title and icon to the GUI
root.title("Waka Ama Sprint Nationals")
root.configure(bg=BG_COLOUR)
root.iconbitmap("icon.ico")

#By: inipagi
#https://icon-icons.com/icon/Trophy-winner-award/82485

# Widgets used in the first GUI window (Label, OptionMenu, and Button)
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