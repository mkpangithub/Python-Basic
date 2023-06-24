import re

txt = "The rain i Spian"

x = re.findall(r"\Bain", txt)

print(x)

if x:
    print("Yes, there is at least one match")
else:
    print("No match")