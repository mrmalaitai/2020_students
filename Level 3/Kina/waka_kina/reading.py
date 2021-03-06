import tkinter as tk
from os import walk

def display_clubs(clubs):
   window = tk.Toplevel(root)
   window.title("Full Club Points")
   window.iconbitmap("waka.ico")
   
   #Turn dict into list
   results = [ [k,v] for k, v in clubs.items() ]
   
   #order list
   results.sort(key = lambda x: x[1])
   print(results)
   #Display list
   results_listbox = tk.Listbox(window, width = 50, height = 50, font = ("Arial", ))
   
   #Adds each waka tot he Listbox "results_listbox"
   for x in results:
   
       if(x[[0][0]] == ""):
           continue
           
       current_waka = "{}".format(x)
       results_listbox.insert(0, current_waka)
       
   results_listbox.grid(row = 0, column = 0)
   print(results)


def calculate_scores(current_year, final_races):
    clubs = {}
    
    for race in final_races:
        current_race = open("{}/{}".format(current_year, race),"r")
        
        
        for club in current_race:
            waka = club.strip().split(",")
            #if("Final" in waka[1]):
            #    break
            
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
    current_years = years_chosen.get()
    
    for root, dirs, files in walk("{}".format(current_years)):
       races.extend(files)
       break
    #print(races)
       
    final_races = []
    
    for race in races:
        if("Final" in race):
            final_races.append(race)
    print(final_races)
    calculate_scores(current_years, final_races)

years = []

for root, dirs, files in walk("."):
   years.extend(dirs)
   break

#
BG_COLOUR = "BLUE"
FG_COLOUR = "WHITE"
root = tk.Tk()

#this code sets the color of my background
root.configure(background = BG_COLOUR)

#this code give me the window title
root.title("Waka Ama Competition")

#this code places my photo of my boat
root.wm_iconbitmap("waka.ico")
title = tk.Label(root, text = "Waka Ama\nCompetition",font = ("Times New Roman", 40),bg = BG_COLOUR, fg = FG_COLOUR)
title.grid(row = 0, column = 0)
#this code give a brief description about the waka ama competition
message = tk.Label(root, text = "At the beginning of each year Nga Kaihoe o Aotearoa, Waka Ama New Zealand hold their annual Sprint Nationals.\n There is a mixture of events at the competition in which regionalassociations compete for medals as well as for the overall association\n of the competition.",font = ("Arial", 12),bg = BG_COLOUR, fg = FG_COLOUR)
message.grid(row = 1, column = 0)
#this code makes you chose a year
years_chosen = tk.StringVar()
years_chosen.set("Select a year:")

years_options = tk.OptionMenu(root, years_chosen, *years)
years_options.grid(row = 2, column = 0)

button = tk.Button(root, text = "Display files", command = display_files,font = ("times new roman", "12"))
button.grid(row = 3, column = 0)

root.mainloop()