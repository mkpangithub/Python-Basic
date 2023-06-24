import re

txt = "The rain in Spian"

x = re.findall("\D", txt)

print(x)

if x:
    print("Yes, there is at least one match")
else:
    print("No match")