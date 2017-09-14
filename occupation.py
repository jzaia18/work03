f = open('occupations.csv','r')
s = f.read()
f.close()

dic = {}
def createDic():
    global dic
    L = s.split('\r\n')
    for lines in L:
        stuff = lines.split(',')
        dic[','.join(stuff[:-1])] = stuff[-1]
