import re

text = 'uduahwudhuahd idnwaundunaund,ad udwna..undunau'
x = re.sub("[.]|[,]|[ ]", ":", text)   #[] return a match for any character of string
print(x)