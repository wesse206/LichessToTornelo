#! ./env/Scripts/pythonw
from tkinter import *
import pgntornelo

root =Tk()
root.title('Lichess to Tornelo')

#Get the lichess tournament tournament link for pgn extraction
tourlinklbl = Label(root, text='Enter the tourament code:')
tourlinklbl.grid(column=0, row=0)
tourlinknty = Entry(root)
tourlinknty.grid(column=1, row=0)

def submit():
    t = tourlinknty.get()
    pgntornelo.worker(t)

submitlink = Button(root, text='Extract', command=submit)
submitlink.grid(column=2, row=0)


root.mainloop()