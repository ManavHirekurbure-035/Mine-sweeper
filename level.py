
from tkinter import *
import settings
LEVEL=0
MINE=0

def on_close(location):
    location.destroy()
    



def level_choice() :
    window = Tk()
    window.title("Level Choice")
    global LEVEL
    global MINE
    level_value = IntVar()

    def level_selected() :
        global LEVEL
        global MINE
        levelSelected = False
        selected_option = level_value.get()
        if selected_option == 1:
            LEVEL = 4
            MINE = 4
            levelSelected = True
        elif selected_option == 2:
            LEVEL = 6
            MINE = 12
            levelSelected = True
        elif selected_option == 3:
            LEVEL = 9
            MINE = 26
            levelSelected = True
        if levelSelected :
            window.destroy()
        
   

    label = Label(window, text="Enter level" , font = ("Ariel", 22, "bold"), width = 20, bg = "#789461", pady=20, padx = 40)
    label.pack()
    easy_btn = Radiobutton(
        window, 
        cursor = "hand2",    
        text = "Easy", 
        variable = level_value, 
        font = ("Comic Sans MS", 16), 
        pady = 10, 
        padx = 10,
        value = 1,

        ).pack(pady = 10)
    medium_btn = Radiobutton(
        window, 
        cursor = "hand2",          
        text = "Medium", 
        variable = level_value, 
        font = ("Comic Sans MS", 16), 
        pady = 10, 
        padx = 10,
        value = 2,

        ).pack(pady = 10)
    hard_btn = Radiobutton(
        window, 
        cursor = "hand2",
        text = "Hard", 
        variable = level_value, 
        font = ("Comic Sans MS", 16), 
        pady = 10, 
        padx = 10,
        value = 3,

        ).pack(pady = 10)


    Button(window, text = "Start Game", padx = 10, pady = 10, font = ("Comic Sans MS", 12), bg = "#F6E6CB", command = level_selected).pack(pady = 20)
    
    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window))

    window.mainloop()    
    return LEVEL, MINE
