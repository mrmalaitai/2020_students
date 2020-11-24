import tkinter as tk
from os import walk


  
def display_clubs(clubs):
    display = tk.Toplevel(root)
    display.title("Full Club Points")
    display.iconbitmap("running.ico")
    
    results = [ [k,v] for k, v in clubs.items()]
    results.sort(key = lambda x: x[1])
    results_listbox = tk.Listbox(display, width = 38, height = 64, font = ("Arial",8))
    for x in results:
        
        if(x[[0][0]] == ""):
            continue
            
        adding_student = "{}".format(x)
        results_listbox.insert(0, adding_student)
        
    results_listbox.grid(row = 0, column = 0)
    print(results)
    
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
    

    
   
    display_clubs(clubs)

def display_files():
    races = []
    current_year = year_chosen.get()

    for root, dirs, files in walk("{}".format(current_year)):
        races.extend(files)
        break
    #print(races)
    
    final_races = []
    
    FINAL_NAMES = ["Final"]
    
    for race in races:
        if("Final" in race):
            final_races.append(race)
    #print(final_races)
    calculate_scores(current_year, final_races)
BG_COLOUR="green"
FG_COLOUR="blue"   
    
years = []

for root, dirs, files in walk("."):
    years.extend(dirs)
    break

# schools = ["Marvel High School", "DC College"]

root = tk.Tk()
root.title("Waka Competition")
root.configure(bg=BG_COLOUR)
root.iconbitmap("running.ico")

title=tk.Label(root,text="Waka Competition",font = ("Calibri",40),bg=BG_COLOUR,fg=FG_COLOUR)
title.grid(row=0,column=0)

message=tk.Label(root,text="Good day the results of the Waka Competition are below. Please select a year below to dispaly the results.",font = ("Calibri",20),bg=BG_COLOUR,fg=FG_COLOUR)
message.grid(row=1,column=0)

year_chosen = tk.StringVar()
year_chosen.set("Choose the year")

year_options = tk.OptionMenu(root, year_chosen, *years)
year_options.grid(row = 2, column = 0)

button = tk.Button(root, text = "Display files", command = display_files)
button.grid(row = 3, column = 0)

root.mainloop()