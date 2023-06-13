#API key: PDOIX0V358OJSYIW alpha_vantage PDOIX0V358OJSYIW
import requests as rq
def get_weekly_price_data(str):
    req = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+str+'&apikey=PDOIX0V358OJSYIW'
    r = rq.get(req)
    data = r.json()
    return(data)
def get_daily_price_data(str):
    req = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+str+'&apikey=PDOIX0V358OJSYIW'
    r = rq.get(req)
    data = r.json()
    return data