#API key: PDOIX0V358OJSYIW alpha_vantage PDOIX0V358OJSYIW
import requests as rq
import json

intervals = ['TIME_SERIES_DAILY_ADJUSTED','TIME_SERIES_WEEKLY','TIME_SERIES_MONTHLY']

def get_price_data(str,call): #
    for interval in intervals:
        if(call.upper() in interval):
            req = 'https://www.alphavantage.co/query?function='+interval+'&symbol='+str+'&apikey=PDOIX0V358OJSYIW'
        else:
            req = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+str+'&apikey=PDOIX0V358OJSYIW'
        r = rq.get(req)
        data = r.json()
    return data
def time_series_weekly(dict1,pastWeeks):
    data = {}
    i = 0
    for k,v in dict1.items():
        if(i == pastWeeks+1):
            break
        data[k] = v
        i += 1
    return data
            
def handle_json(data,deserialize):
    #opens testFile.json and writes output of API call to file
    if deserialize == False:
        with open("testFile.json","w") as write_file:
            json.dump(data,write_file)
    #directly handles JSON and converts to python dictionary with two dictionaries,
    # one contains the time series w a dictionary for each week
    else:
        json_list = json.dumps(data)
        list1 = json.loads(json_list)
        return list1
