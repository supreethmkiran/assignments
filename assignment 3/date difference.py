
import datetime
print(datetime.datetime.today())
y=datetime.date(int(input("enter year")),int(input("enter month")),int(input("enter date")))
print(y)
diff=datetime.date.today()-y
print(diff)
