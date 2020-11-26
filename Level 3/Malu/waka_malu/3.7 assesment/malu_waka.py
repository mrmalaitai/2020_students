#Created by: Maluofenua Sautia
#Date: 03/11/2020

# These allow for GUI to be created, read dirs and files
import tkinter as tk
from os import walk



def show_clubs(clubs):
    show = tk.Toplevel(root)
    show.title("Full Club Points")
    show.iconbitmap("waka.ico")
    
    #this code is for to turn the dict to list
    results = [ [k,v] for k, v in clubs.items() ]
    
    
    #this code is to put the points in Order list
    results.sort(key = lambda x: x[1])
    
    #this code is the show code
    results_listbox = tk.Listbox(show, width = 38, height = 64, font = ("Arial",8), bg=BG_COLOR)
    
    # Adds each waka to the listbox "result_listbox"
    for x in results:
    
        if(x[[0][0]] == ""):
            continue
            
        adding_student = "{}".format(x)
        results_listbox.insert(0, adding_student)
        
    results_listbox.grid(row = 0, column = 0)
    print(result)

    
def calculate_scores(current_year, final_races):
    clubs = {}
    
    for race in final_races:
        current_race = open("{}/{}".format(current_year, race),"r")
        
        
        for club in current_race:
            waka = club.strip().split(",")
                
            score = 0
                
            if(waka[0] == "1"):
                score = 8
            elif(waka[0] == "2"):
                score = 7
            elif(waka[0] == "3"):
                score = 6
            elif(waka[0] == "4"):
                score = 5
            elif(waka[0] == "5"):
                score = 4
            elif(waka[0] == "6"):
                score = 3
            elif(waka[0] == "7"):
                score = 2
            else:
                score = 1
                    
            if(waka[5] not in clubs):
                clubs[waka[5]] = score
            else:
                clubs[waka[5]] = clubs.get(waka[5]) + score
               
    
    current_race.close()
    
    show_clubs(clubs)
    
def show_files():
    races = []
    current_year = year_chosen.get()
    
    for root, dirs, files in walk("{}".format(current_year)):
        races.extend(files)
        break
    print(races)
    
    final_races = []
    
    FINAL_NAMES = ["Final"]
    
    for race in races:
        if("Final" in race):
            final_races.append(race)
    #print(final_races)
    calculate_scores(current_year, final_races)
    
years = []

# Loops through and finds the names of directories in either 2017 or 2018 folders
for root, dirs, files in walk("."):
    years.extend(dirs)
    break


        
    
# schools = ["Marvel High School", "DC College"]
BG_COLOR = "#00FFFF"
FG_COLOR = "#000000"
root = tk.Tk()
root.title("Waka comp Results")
root.iconbitmap("waka.ico")
#This code is for background color
root.configure(bg= BG_COLOR)

#this gives me the title
title = tk.Label (root, text = "Waka Ama \n Competition", font = ("Arial", 30), bg = BG_COLOR, fg = FG_COLOR)
title.grid (row = 0, column = 1)

#this code is for the text after my title
text = tk.Label (root, text = "Welcome to the Waka Ama comp result Site \n on here we have the 2017 & 2018 Comptetion results", font = ("Arial", 12), bg = BG_COLOR, fg = FG_COLOR)
text.grid (row = 1, column = 1)

#this gives me the option menu for the years for the waka ama comp
year_chosen = tk.StringVar()
year_chosen.set("Choose a year")
year_options = tk.OptionMenu(root, year_chosen, *years)
year_options.grid(row =2 , column = 1)

#this is a empty label code
Empty = tk.Label (root, text = " ", bg = BG_COLOR)
Empty.grid (row = 4, column = 1)

#this code gives me the button to show the waka ama comp points 
button = tk.Button(root, text = "Show files", command = show_files)
button.grid(row = 4, column = 1)



root.mainloop()