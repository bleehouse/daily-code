def readNamesByFile(fileName):
    personinfos = []
    personinfoArr = []
    file = open(fileName)
    maxleng = 10
    for line in file:
        personinfoArr = str(line).rstrip('\r\n').split(",")
        personinfos.append({"Last": personinfoArr[0], "First": personinfoArr[1], "Salary": personinfoArr[2]})
        if max(len(personinfoArr[0]), len(personinfoArr[1]), len(personinfoArr[2])) > maxleng:
            maxleng = max(len(personinfoArr[0]), len(personinfoArr[1]), len(personinfoArr[2]))

    print('{:{n}s} {:{n}s} {:{n}s}'.format("Last", "First", "Salary", n=maxleng))
    print("-" *(maxleng*3))
    for personinfoDict in sorted(personinfos, key=lambda k: k['Salary']):
        print('{:{n}s} {:{n}s} {:{n}s}'.format(personinfoDict["Last"], personinfoDict["First"], format(int(personinfoDict["Salary"]),",d"), n = maxleng))

readNamesByFile("name.csv")
