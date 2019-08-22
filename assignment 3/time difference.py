import datetime
x=datetime.datetime.now()
print("Current time in India :",x)
NY=x-datetime.timedelta(hours=9,minutes=30)
SY=x-datetime.timedelta(hours=5,minutes=30)
JO=x-datetime.timedelta(hours=3,minutes=30)
print("New York ",NY)
print("Sydney ",SY)
print("Johannesburg ",JO)


