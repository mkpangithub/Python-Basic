import re

txt = "hello world"

x = re.findall("^hello", txt)

if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")