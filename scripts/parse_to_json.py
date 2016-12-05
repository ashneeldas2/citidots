import pandas as pd
import json
import re
import traceback
import sys

def formatTime(o):
    x = str(o)
    return int(x[8:9])*86400 + int(x[11:13])*3600 + int(x[14:16])*60 + int(x[17:19])

def parse(filename,rows,clump):
    try:
        df = pd.read_csv('../data/'+filename)
    except IOError:
        print "Invalid filename or path."
        sys.exit()
        
    df = df[ ['tripduration','starttime','stoptime','start station latitude','start station longitude','end station latitude','end station longitude','bikeid'] ] # removes unnecessary data
    
    df['starttime'] = df['starttime'].apply(formatTime)
    df['stoptime'] = df['stoptime'].apply(formatTime)
    M = {}

    try:
        rows = int(rows)
    except ValueError:
        if rows == 'all':
            rows = len(df)
        else:
            print "Invalid arguments."
            sys.exit()
        
    for r in range(0, rows):
        
        row = df.iloc[r:r+1]
        M[int(row['bikeid'])] = {
            "starttime": int(row['starttime'])%clump,
            "endtime": int(row['starttime'])%clump + int(row['tripduration']),
            "startLoc": [ float(row['start station latitude']), float(row['start station longitude']) ],
            "endLoc": [ float(row['end station latitude']), float(row['end station longitude']) ],
            }
        sys.stdout.write("\rwrote %d entries" % (r+1))
        sys.stdout.flush()
    text = json.dumps(M)
    f = open('../data/data-'+filename[:-4]+'.json','w')
    f.write(text)
    f.close()

    print '\nTask completed.'

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "usage: python parse_to_json.py [filename rows [clump]]"
        sys.exit()
    
    filename = sys.argv[1]
    rows = sys.argv[2]
    
    if len(sys.argv) == 4:
        clump = int(sys.argv[3])
    else:
        clump = 10**10
        
    parse(filename,rows,clump)
