import re
 
input = ("shanmathi@gmail.com:")

m = re.match('\d{5}\Z',input)
 
if m:
    print("True")
else:
    print("False")
