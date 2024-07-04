from tkinter import *
import settings
import utils

from cell import Cell

root = Tk()
#override settings of window
root.configure(bg='#F6E6CB')
# root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Mine Sweeper')
root.resizable(False,False)

top_frame=Frame(
    root,
    bg='#789461',
    width=settings.WIDTH,
    height=utils.height_prct(5)
) 
top_frame.pack(fill ="x")

game_tile=Label(
    top_frame,
    bg = "#789461",    
    text='Mine Sweeper',
    font=('Comic Sans MS',35,"bold")
)
game_tile.pack(pady = 10)

count_frame=Frame(
    root,    
    bg='#F6E6CB',
    width=settings.WIDTH,
    height=utils.height_prct(10),
    pady = 10     
)
count_frame.pack ()




center_frame=Frame(
    root,
    bg = "#F6E6CB",
    width=utils.width_prct(80),
    height=utils.height_prct(80) ,
    pady = 15  
)
center_frame.pack()
# place(x=utils.width_prct(20),y=utils.height_prct(20))
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=Cell(x,y)
        c.create_btnobj(center_frame)
        c.cellbtn.grid(
            column=x,
            row=y
        )
#call label from cell
Cell.create_cellcount_label(count_frame)
Cell.create_minecount_label(count_frame)
Cell.cell_count_label_object.pack(side = LEFT, padx = 40)
Cell.mine_count_label_object.pack(side = LEFT, padx = 40)
Cell.randomine_mines()

  

#run window
root.mainloop()

