import price
import handler as hd
import annual_series as ap
import volume as vl
import matplotlib.pyplot as plt
import pandas as pd
import analysis
import numpy as np
def main():
   interactive = False
   if interactive:
      print("what equity would you like to see?")
      strS = input()
      print("what calendar year would you like to view?")
      strY = input()
   else:
      strS = 'TSLA'
      strY = '2023'
   data =  price.get_weekly_price_data(strS)
   dict1 = hd.handle_json(data,True)
   year = ap.time_series_recent(dict1["Weekly Time Series"],strY)
   a = analysis.Analysis(strY,datadic=year)
   list1 = ["Open","High","Low","Close","Volume"]
   a.cleaner()
   a.fill_data(1,2)
   #li = a.datadic.values()
   #print(li.values())
   plt.plot(a.dates,a.data1,'r--',a.data2,'b--')
   ax = plt.gca()
   ax.set_xticks(ax.get_xticks()[::5])
   plt.ylabel(list1[1] + " & " + list1[2])
   plt.show()

   #print(type(dict1["Weekly Time Series"]["2023-05-31"]))


main()
