cnt = 999

while cnt < 10000:
    cnt = cnt + 1
    reversenum = int(str(cnt)[::-1])

    num1 = int(str(cnt)[0:1])
    num2 = int(str(cnt)[1:2])
    num3 = int(str(cnt)[2:3])
    num4 = int(str(cnt)[3:4])

    calnum1 = num1 * num2 * num3 * num4
    calnum2 = int(str(num1) + str(num2)) * num3 * num4
    calnum3 = int(str(num1) + str(num2) + str(num3))*num4
    calnum4 = num1 * int(str(num2) + str(num3))*num4
    calnum5 = num1 * num2 * int(str(num3) + str(num4))
    calnum6 = num2 * num3 * int(str(num1) + str(num4))

    if calnum1 == reversenum:
        print(reversenum)
        print(cnt)
    if calnum2 == reversenum:
        print(reversenum)
        print(cnt)
    if calnum3 == reversenum:
        print(reversenum)
    if calnum4 == reversenum:
        print(cnt)
        print(reversenum)
    if calnum5 == reversenum:
        print(reversenum)
        print(cnt)
    if calnum6 == reversenum:
        print(reversenum)
        print(cnt)

