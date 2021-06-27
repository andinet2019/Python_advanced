myfile=open("fruit.txt")
print(myfile.read())
myfile.close()
# with open doesnot need closing file
with open ("fruit.txt") as myfile:
    content=myfile.read()
print(content)
#writing  on files
with open("docmanu/pinam.txt", "w") as file1:
    file1.write("peanguin\n Onion\nJava")

