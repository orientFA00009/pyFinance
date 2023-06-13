#returns a dictionary with the most recent calendar year in 
#to be reworked
def time_series_recent(dict1,strY):
    year = {}
    for k,v in dict1.items():
        if(k[:4] == strY):
            year[k] = v
    return year
            
