#! ./env/Scripts/pythonw
from tkinter import *
from tkinter.filedialog import askdirectory
import pgntornelo
from pathlib import Path


root =Tk()
root.title('Lichess to Tornelo')
root.resizable(False, False)

linkframe = Frame(root, borderwidth=1, relief='groove')
outdirframe = Frame(root, borderwidth=1, relief='groove')
linkframe.grid(row=0, column=0, sticky=W)
outdirframe.grid(row=1, column=0, sticky=W)

tourlinklbl = Label(linkframe, text='Enter the tourament code:')
tourlinklbl.grid(column=0, row=0, sticky=W)
tourlinknty = Entry(linkframe)
tourlinknty.grid(column=1, row=0, sticky=W)
# Get the lichess tournament tournament link for pgn extraction

outdirlbl = Label(outdirframe, text='Choose your output directory:')
outdirlbl.grid(column=0, row=0, sticky=E)
outdirnty = Entry(outdirframe, width=40)
outdirnty.insert(0, str(Path.home())+'\\Documents')
outdirnty.grid(column=1, row=0, sticky=W)
# Get the output directory for the pgn file


def submit():
    t = tourlinknty.get()
    o = outdirnty.get()
    pgntornelo.worker(t, o)

def browse():
    outdir = askdirectory(title='Choose a directory')
    outdirnty.delete(0, END)
    outdirnty.insert(0, outdir)

browsebtn = Button(outdirframe, text='Browse', command=browse)
submitlink = Button(linkframe, text='Extract', command=submit)
browsebtn.grid(column=2, row=0)
submitlink.grid(column=2, row=0, sticky=W)


root.mainloop()