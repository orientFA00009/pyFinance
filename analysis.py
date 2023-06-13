from typing import Any


class Analysis:
    #analysis obj takes
    def __init__(self,name,datadic,aspect1,aspect2):  
        self.name = name
        self.dataTuple = []   #hold all relevant data(open,close,high,low,volume in a list of tuple)
        self.dates = []
        self.data1 = []
        self.data2 = []
        for k,v in datadic.items():     #(k,v) ---> ("01-20-2023", ['1.open': 123.0....'5. volume' : 1232424])
            self.dates.append(k) 
            for k1,v1 in v.items():
                if aspect1 in k1:
                    self.data1.append(v1)
                elif aspect2 in k1:
                    self.data2.append(v1)
            #self.dataTuple.append((float(v['1. open']),float(v['2. high']),float(v['3. low']),float(v['4. close']),int(v['5. volume'])))
        
        
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
    def get_data1(self):
        return self.data1
    def get_data2(self):
        return self.data2
    #will clean data before processing in matplotlib/pandas, data will be in a list
    #from weekly time series, grab opening values and closing values
    #tuple holds values (date,open,high,low,close,volume)
        

    # def fill_data(self,index,index1):
    #     list1 = []
    #     list2 = []
    #     for val in self.dataTuple:
    #         list1.append(val[index])
    #         list2.append(val[index1])
    #     self.data1 = list1
    #     self.data2 = list2