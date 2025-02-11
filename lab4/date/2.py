from datetime import date, timedelta

yesterday = date.today() - timedelta(1)
today = date.today()
tomorow = date.today() + timedelta(1)

print(yesterday)
print(today)
print(tomorow)
