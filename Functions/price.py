
import requests as rq
def get_price(str):
    req = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+str+'&apikey=PDOIX0V358OJSYIW'
    r = rq.get(req)
    data = r.json()
    return(data)

