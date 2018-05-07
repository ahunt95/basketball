import sys
import numpy as np
import pandas as pd
import csv
from datetime import datetime

with open (sys.argv[1], newline='') as csvfile: # Input unclean data
    filereader = csv.reader(csvfile)
    header = next(filereader) # First line is a header	
    data = [] # data = [row[1], row[2], ... row[N]]
    for row in filereader:
        date = datetime.strptime(row[0], '%b %d, %Y').date()
        #opponent = row[1]
        if row[1][0] == 'v':
            opponent = row[1][3:]
            home = 1
            away = 0
        else:
            opponent = row[1][2:]
            home = 0
            away = 1

        game = row[2]
        result = row[3]
        score = row[4]
        token1 = row[4].split('-')
        team_score = int(token1[0])
        opponent_score = int(token1[1])
        ats = row[5]
        #spread = float(row[6])
        if row[6] == 'Ev':
            spread = float(0)
        else:
            spread = float(row[6])
        ou = row[7]
        total = float(row[8])
        team = row[9][1:-15]

        data.append([date, opponent, home, away, game, result, team_score, 
                     opponent_score, ats, spread, ou, total, team])

    path = '/home/aaron/PHYS476/project/spread_data.csv'
    file = open(path, 'w')
    writer = csv.writer(file)
    # Write header
    writer.writerow(['date',
                     'opponent',
                     'home',
                     'away',
                     'game',
                     'result',
                     'team_score',
                     'opponent_score',
                     'ats',
                     'spread',
                     'ou',
                     'total',
                     'team'])

    for drow in data:
        date = drow[0]
        opponent = drow[1]
        home = drow[2]
        away = drow[3]
        game = drow[4]
        result = drow[5]
        team_score = drow[6]
        opponent_score = drow[7]
        ats = drow[8]
        spread = drow[9]
        ou = drow[10]
        total = drow[11]
        team = drow[12]

        writer.writerow([date, opponent, home, away, game, result, 
                         team_score, opponent_score, ats, spread, ou, 
                         total, team])

    file.close()