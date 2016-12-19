# quiz 21

i = 0
j = 0

pyramid = []
zerocount = 0

while True:
    row = []
    while True:
        if j < 1:
            row.append(1)
        elif j >= 1 and j < i:
            if pyramid[i-1][j-1] == 1 and pyramid[i-1][j] == 0:
                row.append(1)
            elif pyramid[i-1][j-1] == 0 and pyramid[i-1][j] == 1:
                row.append(1)
            else:
                row.append(0)
                zerocount = zerocount + 1
                if zerocount > 2013:
                    break
        else:
            row.append(1)
        if j == i:
            break
        j = j + 1
    if zerocount > 2013:
        print("match count : " + str(i+1))
        break
    pyramid.append(row)
    row = []
    j = 0
    i = i + 1
