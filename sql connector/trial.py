import mysql.connector




con=mysql.connector.connect(host="localhost",user="root",password="root",database="supreeth")
print(con)
my=con.cursor()
def printer():
        sql1="select * from odi"
        my.execute(sql1)
        l=my.fetchall()
        for i in l:
                print(i)
printer()
print()
print()

my.execute("insert into ODI values(16,16,'Austria',22,146,23,0)")
printer()
print()
print()

my.execute("update ODI set team='Russia' where team_id=16")
printer()

print()
print()



my.execute("delele from odi where TEAM_ID=16")
printer()

print('1.update Ranks')
print("2.update Name")
print("3.update Points")
ch=int(input('Enter your choice: '))
if ch=1:
	my.execute("update odi set rank=rank+1 where rank in (12,3,4,5,6,7,8,9)and rank =1 where rank=10 ")
	printer()
elif ch=2:
	my.execute("update odi set name = 'England' where  ")
