import re

txt = "That will be 59 dollers"

x = re.findall("\d", txt)

print(x)