import re

txt = "hello world"

x = re.findall("world$", txt)
if x:
    print("Yes, the string ends with 'world'")
else:
    print("No match")