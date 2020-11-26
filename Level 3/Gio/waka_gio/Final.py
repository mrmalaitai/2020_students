# Created by: Giovaani

import tkinter as tk
from os import walk

# Displays the clubs for the Waka competition
def display_clubs(clubs):
    display = tk.Toplevel(root)
    display.title("All Club Points")
    display.iconbitmap("WakaAma.ico")
    
    #Turn dict into list
    results = [[k,v] for k, v in clubs.items()]
    
    # Order list
    results.sort(key = lambda x: x[1])
    
    # Display list
    results_listbox = tk.Listbox(display, width = 36, height = 64, font = ("Ariel", 8))
    print(results)
    # Adds each waka to the Lsitbox "results_listbox"
    for x in results:
        
        if(x[[0][0]] == ""):
            continue
            
        adding_student = "{}".format(x)
        results_listbox.insert(0, adding_student)

    results_listbox.grid(row = 0, column = 0)
    print(results)
    
    results = tk.Listbox(display)
    for x in races:
        adding_race = "{} {}".format(races[x], x)
        results.insert(0, adding_race)

    results.grid(row = 0, column = 0)


# Calculates the scores for each Waka team
def calculate_scores(current_year, final_races):
    clubs = {}
    
    for race in final_races:
        current_race = open("{}/{}". format(current_year, race),"r")
        
        
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
        

    
            # Converting into dictionary list
    print(clubs)
    display_clubs(clubs)

# Displays the files for the user to choose from
def display_files():
    races = []
    current_year = year_chosen.get()
    
    # Loops through all races in the directory and adds to a list
    for root, dirs, files in walk("{}".format(current_year)):
        races.extend(files)
        break
        
    final_races = []
        
    # Loops through all races and finds "Final" races    
    for race in races:
        if("Final" in race):
            final_races.append(race)
        
    calculate_scores(current_year, final_races)
    
    
years = []

# for loop for looking through folders in the 2017 folder or 2018 folder
for root, dirs, files in walk("."):
    years.extend(dirs)
    break

# CONSTANTS
# The Background Colour
BG_COLOUR="#C933FF"# Purple
# The Font Colour
FG_COLOUR="#5FFF33"# Green
root = tk.Tk()

# Providing an icon and title for the GUI
root.title("Waka Ama Competition")
root.configure(bg=BG_COLOUR)
root.iconbitmap("WakaAma.ico")
root.geometry("400x150")

# Title label for user to see
title = tk.Label(root, text="The Waka Ama Spring National Competition", font = ("Ariel", [14]), bg=BG_COLOUR, fg=FG_COLOUR)
title.grid(row = 0, column = 0)

# Message label
title = tk.Label(root, text = "Champions of 2017 & 2018", font = ("Ariel", [14]), bg=BG_COLOUR, fg=FG_COLOUR)
title.grid(row = 1, column = 0)

# Default "Select Year" for OptionMenu widget
year_chosen = tk.StringVar()
year_chosen.set("Select Year")

# OptionMenu widget to choose folder
year_options = tk.OptionMenu(root, year_chosen, *years)
year_options.grid(row = 3, column = 0)

# Button for user to display folders (2017, 2018)
button = tk.Button(root, text = "Display files", command = display_files)
button.grid(row = 4, column = 0)

root.mainloop()