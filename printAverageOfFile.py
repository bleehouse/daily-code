def printAverageOfFile(fileName):
    sum = 0
    count = 0

    file = open(fileName)
    for line in file:
        n = int(line)
        sum += n
        count += 1
    print("Average og numbers in " + fileName + ":")
    print(sum/count)

printAverageOfFile("1.txt")