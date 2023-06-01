class Analysis:
    #analysis obj takes
    def __init__(self,name,datadic):
        #self.interval = interval
        self.name = name
        self.datadic = datadic
        self.open = []
        self.close = []
        self.dates = []
   # def get_interval(self):
    #    return self.interval
    #def set_interval(self, new_interval):
    #    self.interval = new_interval
    def get_name(self):
        return self.name
    def set_name(self, n):
        self.name = n
    def get_datadic(self):
        return self.datadic
    #will clean data before processing in matplotlib/pandas, data will be in a list
    #from weekly time series, grab opening values and closing values
    def cleaner(self):
        for k,v in self.datadic.items():
            self.dates.append(k)
            self.open.append(float(v['1. open']))
            self.close.append(float(v['4. close']))
            