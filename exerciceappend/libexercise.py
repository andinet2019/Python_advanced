#append and read at same time with python
import os
import time
import pandas
if os.path.exists("file/addresses.csv"):
  data=pandas.read_csv("file/addresses.csv")
  print(data.mean())
else:print("file does not exist")
time.sleep(15)

