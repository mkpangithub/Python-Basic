import re

txt = "8 times before 11:45 AM"

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")