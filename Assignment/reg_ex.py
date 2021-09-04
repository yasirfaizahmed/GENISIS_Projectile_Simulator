import re

fp = open("sample.txt")
for line in fp:
    if re.search(r"4561237890", line):
        print(line.rstrip())
#    if re.search(r"name1@gmail.com", line):
#        print(line.rstrip())

fp.close()
