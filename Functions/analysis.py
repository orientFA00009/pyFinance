class Analysis:
    #analysis obj takes
    def __init__(self,name,datadic):
        #self.interval = interval
        self.name = name
        self.datadic = datadic
        #hold all relevant data(open,close,high,low in a list of tuple)
        #self.open = []
        self.dataTuple = []
        #self.close = []
        self.dates = []
        self.data1 = []
        self.data2 = []
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
    #tuple holds values (date,open,high,low,close,volume)
    def cleaner(self):
        for k,v in self.datadic.items():
            self.dates.append(k)
            self.dataTuple.append((float(v['1. open']),float(v['2. high']),float(v['3. low']),float(v['4. close']),int(v['5. volume'])))

    def fill_data(self,index,index1):
        list1 = []
        list2 = []
        for val in self.dataTuple:
            list1.append(val[index])
            list2.append(val[index1])
        self.data1 = list1
        self.data2 = list2
