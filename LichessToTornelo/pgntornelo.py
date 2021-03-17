import requests
def downloadpgn(tournlink):
    tournfiler = requests.get('https://lichess.org/api/swiss/'+tournlink+'/games', allow_redirects=True)
    open('tournament.pgn', 'wb').write(tournfiler.content)

# Function to download the tournament file. The tournlink param gets feeded from the worker function.
def convertpgn(tournfile, outfile=None):
    count = len(open('tournament.pgn').readlines(  ))
    totalcount = count/20/5
    # Count the players to know how much profiles to edit

    with open('tournament.pgn', 'r+') as f:
        lines = f.readlines()
        round = 1
        roundline = -1
        for i, line in enumerate(lines):
            if line.startswith('[Date "'):
                roundline += 1
                if roundline == totalcount:
                    round += 1
                    roundline = 0
                lines[i] = lines[i].strip() + ' [Round "%s"]\n' % str(round)
        f.seek(0)
        for line in lines:
            f.write(line)
    # Adds the rounds per total games per round

def worker(sendtodwnld=None, outdir=None):
    downloadpgn(sendtodwnld)
    convertpgn('tournament.pgn')
# Function to lead the program to download the files. Accessed by the main file.