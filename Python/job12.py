import re

file = open("data.txt")
text = file.read()
pattern = '[a-zA-Z]+'
matches = re.findall(pattern, text)

print(len(matches))