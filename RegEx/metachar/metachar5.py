import re

txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("aix*", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")