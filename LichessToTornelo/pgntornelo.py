import requests
def downloadpgn(tournlink):
    tournfiler = requests.get('https://lichess.org/api/swiss/'+tournlink+'/games', allow_redirects=True)
    open('tournament.pgn', 'wb').write(tournfiler.content)

# Function to download the tournament file. The tournlink param gets feeded from the worker function.
def convertpgn(tournfile, outfile=None):
    count = 0
    
    with open('tournament.pgn', 'r+') as c:
        linec = c.readlines()
        for i, line in enumerate(linec):
            if line.startswith('[Event '):
                count += 1
    count /= 5
    # Count the players to know how much profiles to edit
    # TODO enhance the counter by matching the UTC times. 

    with open('tournament.pgn', 'r+') as f:
        lines = f.readlines()
        round = 1
        roundline = -1
        for i, line in enumerate(lines):
            if line.startswith('[Date "'):
                roundline += 1
                if roundline == count:
                    round += 1
                    roundline = 0
                lines[i] = lines[i].strip() + ' [Round "%s"]\n' % str(round)
        f.seek(0)
        for line in lines:
            f.write(line)
    # Adds the rounds per total games per round

'''
    with open('tournament.pgn', 'r+') as w:
        linew = w.readlines()
        for i, line in enumerate(linew):
            if line.startswith('[White ') or line.startswith('[Black '):
                w.seek(8)
                w.write('L, ')
# Trying to add a firstname of each player, but still failing 
'''

def worker(sendtodwnld=None, outdir=None):
    downloadpgn(sendtodwnld)
    convertpgn('tournament.pgn')
# Function to lead the program to download the files. Accessed by the main file.