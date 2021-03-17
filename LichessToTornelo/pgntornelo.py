import requests
def downloadpgn(tournlink):
    tournfiler = requests.get('https://lichess.org/api/swiss/'+tournlink+'/games', allow_redirects=True)
    open('tournament.pgn', 'wb').write(tournfiler.content)

# Function to download the tournament file. The tournlink param gets feeded from the worker function.
def convertpgn(tournfile, outfile=None):
    count = len(open('tournament.pgn').readlines(  ))
    totalcount = count/20/5*2
    # Count the players to know how much profiles to edit





def worker(sendtodwnld=None, outdir=None):
    downloadpgn(sendtodwnld)
    convertpgn('tournament.pgn')
# Function to lead the program to download the files. Accessed by the main file.