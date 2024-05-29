import datetime as dt

now = dt.datetime.now()

if now.year == 2024:
    print("B.E. Completed")
print(type(now.year))

date_of_birth = dt.datetime(year=2002, month=4, day=25)
print(date_of_birth)
