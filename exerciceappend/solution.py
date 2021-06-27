#append and read at same time with python
import os
import time
if os.path.exists("file/data.txt"):
  with open("file/data.txt", "a+") as file:
    file.seek(0)
    content= file.read()
    file.seek(0)
    file.write(content)
    file.write(content)
else:print("file does not exist")
time.sleep(15)

