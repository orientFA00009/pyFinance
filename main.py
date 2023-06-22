import price
import handler as hd
import volume as vl
import matplotlib.pyplot as plt
import pandas as pd
import analysis
import numpy as np
def main():
   interactive = True
   if interactive:
      print("what equity would you like to see?")
      strS = input()
   else:
      strS = 'TSLA'
   data =  price.get_price_data(strS,"weekly")
   dict1 = price.handle_json(data,1)
   print(type(dict1))
   dataPoints = 1000
   year = price.time_series_weekly(dict1["Weekly Time Series"],dataPoints) # max 1039
   print(len(year))
   a = analysis.Analysis(year,'open','close')
   list1 = ["Open","High","Low","Close","Volume"]
   print(len(a.data1))
   print(len(a.data2))
   plt.plot(a.dates,a.data1,'r--',a.data2,'b--')
   ax = plt.gca()
   ax.set_xticks(ax.get_xticks()[::round(dataPoints/10.4)])
   plt.ylabel(list1[1] + " & " + list1[2])
   plt.show()

   #print(type(dict1["Weekly Time Series"]["2023-05-31"]))


main()