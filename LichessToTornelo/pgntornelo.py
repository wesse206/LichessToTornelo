import requests
import shutil, os
from pathlib import Path
from tkinter import messagebox

def downloadpgn(tournlink):
    tournfiler = requests.get('https://lichess.org/api/swiss/'+tournlink+'/games', allow_redirects=True)
    open('tournament.pgn', 'wb').write(tournfiler.content)
# Function to download the tournament file. The tournlink param gets feeded from the worker function.

def convertpgn(tournfile, outdir, outfile):
    count = 0
    
    with open('tournament.pgn', 'r+') as c:
        lines = c.readlines()
        prevline = 0
        gamesperround = 1
        roundtotal = 0
        for i, line in enumerate(lines):
            if line.startswith('[UTCTime'):
                count += 1
                if prevline == line:
                    gamesperround += 1
                    lines[i] = lines[i].strip() + ' [Round "%s.%s"]\n' % (str(roundtotal), gamesperround)
                else:
                    gamesperround = 1
                    roundtotal += 1
                    lines[i] = lines[i].strip() + ' [Round "%s.%s"]\n' % (str(roundtotal), gamesperround)
                prevline = line
        count /= roundtotal
    # Adds the rounds to the file per time


    with open('tournament.pgn', 'r+') as w:
        linew = w.readlines()
        for i, line in enumerate(linew):
            if line.startswith('[White '):
                linelen = 8-len(line) 
                lines[i] = line[:8] + 'L, ' + line[linelen:]
        w.seek(0)
        for line in lines:
            w.write(line)
        for i, line in enumerate(linew):
            if line.startswith('[Black '):
                linelen = 8-len(line)
                lines[i] = line[:8] + 'L, ' + line[linelen:]
        w.seek(0)
        for line in lines:
            w.write(line)
# Adds a 'L, ' in front of every player, so that Tornelo can accept the pgn    
            
    home = str(Path.home())
    shutil.copyfile('./tournament.pgn', outdir + '\\%s.pgn' % outfile)
    os.remove('tournament.pgn')

    messagebox.showinfo(title='PGN Conversion completed', message='The PGN was converted succesfully and ready to upload to Tornelo')

def worker(sendtodwnld, outdir, outfile):
    downloadpgn(sendtodwnld)
    convertpgn('tournament.pgn', outdir, outfile)
# Function to lead the program to download the files. Accessed by the main file.