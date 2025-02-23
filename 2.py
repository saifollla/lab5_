import re

text = "msdfnsjandaasacaabbbsdfsdsd"
x = re.search('abb|abbb', text)
print(x)