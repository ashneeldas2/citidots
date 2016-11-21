import pandas as pd
import json
import re

def formatTime(o):
    x = str(o)
    return int(x[8:9])*86400 + int(x[11:13])*3600 + int(x[14:16])*60 + int(x[17:19])

def parse(filename):
    df = pd.read_csv(filename)
    df = df[ ['starttime','stoptime','start station latitude','start station longitude','end station latitude','end station longitude','bikeid'] ] # removes unnecessary data
    
    df['starttime'] = df['starttime'].apply(formatTime)
    df['stoptime'] = df['stoptime'].apply(formatTime)
    M = {}
    for r in range(0, 1000):
        row = df.iloc[r:r+1]
        M[int(row['bikeid'])] = {
            "starttime": int(row['starttime']),
            "endtime": int(row['stoptime']),
            "startLoc": [ float(row['start station latitude']), float(row['start station longitude']) ],
            "endLoc": [ float(row['end station latitude']), float(row['end station longitude']) ],
            }
    text = json.dumps(M)
    f = open('data.json','w')
    f.write(text)
    f.close()

d = parse('../data/d.csv')
