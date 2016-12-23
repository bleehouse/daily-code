import datetime

start_date = str(input("Enter start date (yyyymmdd) : "))
end_date = str(input("Enter end date (yyyymmdd) : "))

date = datetime.datetime(
    int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:])
    )

while True:
    date += datetime.timedelta(days=1)
    today = str(date.strftime('%Y%m%d'))
    today_decimaltobin = str(bin(int(today)))[2:]
    today_bintodecimal = str(int(str(today_decimaltobin)[::-1], 2))
    if today == end_date:
        break
    if (today == today_bintodecimal):
        print(today)
