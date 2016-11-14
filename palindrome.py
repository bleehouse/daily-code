
magic_number = 100

while True:
    cnt=cnt+1
    if cnt > 9:
        countToStr = str(cnt)
        temp = round(len(countToStr)/2)
        if countToStr[0:temp] == countToStr[temp:] :
            print(countToStr[0:temp] + " " + countToStr[temp:])
            break
        
