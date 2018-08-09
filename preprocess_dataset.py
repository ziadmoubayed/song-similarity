import re
from datetime import datetime

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Every dataset is lower cased except for TREC
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string).strip()     
    string = re.sub(r"\'s", "'s", string) 
    string = re.sub(r"\'ve", "\'ve", string) 
    string = re.sub(r"n\'t", "n\'t", string) 
    string = re.sub(r"\'re", "\'re", string) 
    string = re.sub(r"\'d", "\'d", string) 
    string = re.sub(r"\'ll", "\'ll", string) 
    string = re.sub(r",", ",", string) 
    string = re.sub(r"!", "", string) 
    string = re.sub(r"\(", "(", string) 
    string = re.sub(r"\)", ")", string) 
    string = re.sub(r"\?", "?", string) 
    string = re.sub(r"\s{2,}", " ", string)  
    string = re.sub(r"\s", "_", string)    
    return  string.strip().lower()

def get_epoch(time):
    p = '%Y-%m-%dT%H:%M:%SZ'
    epoch = datetime(1970, 1, 1)
    return (datetime.strptime(time, p) - epoch).total_seconds() * 1000

def is_old(time1, time2):
    return abs(get_epoch(time2) - get_epoch(time1)) > 720000

current = '2006-05-04T23:08:57Z'

with open('./lastfm-dataset-1K/userid-timestamp-artid-artname-traid-traname.tsv') as f:
    with open('./lastfm-dataset-1K/processed.txt', 'a') as the_file:
        for line in f:
            fields = re.split(r'\t+', line)
            old = is_old(fields[1], current)
            user = fields[0]
            track = clean_str(fields[len(fields) -1])
            current = fields[1] #changed time..
            #print(user, old, track, current)
            if(old):
                the_file.write('\n')
            if(track):
                the_file.write(track + ' ')
# you may also want to remove whitespace characters like `\n` at the end of each line

