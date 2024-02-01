from datetime import datetime,timedelta
offset_india=timedelta(hours=05.30)
print("india offset",offset_india)
offset_usa=timedelta(hours=-12.00)
print("usa offset",offset_usa)

time_country1=datetime.utcnow()+offset_india
print("first",time_country1)

time_country2=datetime.utcnow()+offset_usa
print("second",time_country2)

time_diff=time_country1-time_country2
print("time fifference:",time_diff.total_seconds())

if time_diff.total_seconds()>0:
    print("ahead")
else:
    print("behind")


