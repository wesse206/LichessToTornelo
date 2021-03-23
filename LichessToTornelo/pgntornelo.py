import requests
def downloadpgn(tournlink):
    tournfiler = requests.get('https://lichess.org/api/swiss/'+tournlink+'/games', allow_redirects=True)
    open('tournament.pgn', 'wb').write(tournfiler.content)

# Function to download the tournament file. The tournlink param gets feeded from the worker function.
def convertpgn(tournfile, outfile=None):
    count = 0
    
    with open('tournament.pgn', 'r+') as c:
        linec = c.readlines()
        prevline = 0
        gamesperround = 1
        roundtotal = 0
        for i, line in enumerate(linec):
            if line.startswith('[UTCTime'):
                count += 1
                if prevline == line:
                    gamesperround += 1
                else:
                    gamesperround = 1
                    roundtotal += 1
                prevline = line
    
        print(roundtotal)
        count /= 5
        print(count)
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


def worker(sendtodwnld=None, outdir=None):
    downloadpgn(sendtodwnld)
    convertpgn('tournament.pgn')
# Function to lead the program to download the files. Accessed by the main file.