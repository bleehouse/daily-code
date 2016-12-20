def readNamesByFile(fileName):
    count = 0
    names = []
    file = open(fileName)
    for line in file:
        names.append(str(line).rstrip('\r\n'))
        count += 1

    names.sort(key=lambda x: x.upper())

    for name in names:
        print(name)

readNamesByFile("names.txt")
