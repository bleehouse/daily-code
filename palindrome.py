
cnt = 9

while True :
    cnt = cnt + 1
    int2bin =  str(bin(cnt))[2:]
    int2oct = str(oct(cnt))[2:]
    if int2bin == int2bin[::-1] and int2oct == int2oct[::-1]  :
        print(int2bin + " " + int2bin[::-1] +  " " )
        print(int2oct + " " + int2oct[::-1] +  " " )
        break
