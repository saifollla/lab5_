import re

text = "aaaabbbbbbbbbb"
x = re.search('a*b*', text)
print(x)