from tkinter import Button,Label
import random
import settings
import ctypes
import sys
class Cell:
    all=[]
    cellcount=settings.CELL_COUNT
    minecount=settings.MINES_COUNT    
    cell_count_label_object=None
    mine_count_label_object=None
    def __init__(self,x,y,ismine=False):
        self.ismine=ismine
        self.is_opened=False
        self.ismine_candidate=False
        self.cellbtn= None
        self.x=x
        self.y=y
        Cell.all.append(self)
#append obj to cell.all list
    def create_btnobj(self,location):
        btn=Button(
            location,
            width=3,
            height=1,
            font = ("Comic Sans MS", 16)            
        )
        btn.bind('<Button-1>',self.left_click)   #left click
        btn.bind('<Button-3>',self.right_click)  #right click
        self.cellbtn=btn

    @staticmethod
    def create_cellcount_label(location):
        lbl=Label(
            location,
            bg='#688B4B',
            
            width = 15,
            text=f"Cells left : {Cell.cellcount}",            
            font=('Comic Sans MS',16),            
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def create_minecount_label(location):
        mine_lbl=Label(
            location,
            bg='#688B4B',
            
            width = 15,
            text=f"Mine left : {Cell.minecount}",            
            font=('Comic Sans MS',16)        
        )
        Cell.mine_count_label_object = mine_lbl

    def left_click(self,event):
        if self.ismine:
            self.show_mine()
        else:
            if self.surrounded_cell_mines_length==0:
                for cell_obj in self.surrounded_cell:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cellcount==settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0,"Congratulations! You won!!","Game over",0)
        
        #cancel click event if cell open
        self.cellbtn.unbind('<Button-1>')
        self.cellbtn.unbind('<Button-3>')

   
        

    def right_click(self,event):
        if not self.ismine_candidate:
            Cell.minecount-=1
            self.cellbtn.configure(
                bg='orange'                 
            )
            
            self.ismine_candidate=True
        else:
            Cell.minecount+=1
            self.cellbtn.configure(
                bg='SystemButtonFace'                
            )
            self.ismine_candidate=False
        
        if Cell.mine_count_label_object:
            Cell.mine_count_label_object.configure(
                text=f"Mine left : {Cell.minecount}"
                )

    def getcell(self,x,y):
        #return cell obj based on x and y
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell
    
    @property
    def surrounded_cell_mines_length(self):
        counter=0
        for cell in self.surrounded_cell:
            if cell.ismine:
                counter+=1
        return counter
    def show_cell(self):
        if not self.is_opened :
            Cell.cellcount-=1     
            self.cellbtn.configure(text=self.surrounded_cell_mines_length)
            #replace text of cell count lable with new count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                text=f"Cells left : {Cell.cellcount}"
                )            
            self.cellbtn.configure(
                bg='SystemButtonFace'
            )
        
        #mark opened cell
        
        self.is_opened=True 

        
    @property
    def surrounded_cell(self):
        cells=[
                self.getcell(self.x-1, self.y-1),
                self.getcell(self.x-1, self.y),
                self.getcell(self.x-1, self.y+1),
                self.getcell(self.x, self.y-1),
                self.getcell(self.x, self.y+1),
                self.getcell(self.x+1, self.y),
                self.getcell(self.x+1, self.y+1),
                self.getcell(self.x+1, self.y-1)
        ]
        cells=[cell for cell in cells if cell is not None]
        return cells


    def show_mine(self):
        self.cellbtn.configure(bg='red') 
        ctypes.windll.user32.MessageBoxW(0,"You clicked on a mine","Game Over",0)
        sys.exit()  
          

    

    @staticmethod
    def randomine_mines():
        picked_cell=random.sample(Cell.all,settings.MINES_COUNT)
        for picked_cells in picked_cell:
            picked_cells.ismine=True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"