with open("text.txt", "r") as file:
    content = file.read()

print(content)

file = open("dairy.txt","w")
file.write("Today i learned python file handling")

file.close()

file = open("dairy.txt","r")
content = file.read()
print(content)
file.close()

file = open("dairy.txt","a")
from datetime import datetime
now = datetime.now()
file.write("\n" + str(now))
file.close()

file = open("dairy.txt","r")
content = file.read()
print(content)
file.close()
           

