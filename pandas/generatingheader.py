import pandas
output=pandas.read_csv("data.txt",header=None)
output.columns=["ID","Address","City","Zip","Country","Name","Employees"]
#to set an index
output2=output.set_index("ID")
print(output2)