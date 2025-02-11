import datetime

date = datetime.date(2025,10, 1)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H %M %S %d %m %y")
#print(now)
#print(today)

target_datetime = datetime.datetime(2010, 1, 30 , 16, 30, 20)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("target date has passed")
else:
    print("target date has not passed")
#print(target_datetime)