import sqlite3

# connect
conn = sqlite3.connect("enterprise.db")
curs = conn.cursor()

try:
    curs.execute("drop table zoo")
except sqlite3.OperationalError as e:
    print("Unbale to drop table: {}".format(e))

# create
curs.execute("""create table zoo
(critter varchar(20) primary key,
count int,
damages float)""")

# insert
ins = "insert into zoo values(?, ?, ?)"
curs.execute(ins, ('duck', 5, 0.0))
curs.execute(ins, ('bear', 2, 1000.0))
curs.execute(ins, ('weasel', 1, 2000.0))

# select
curs.execute("select * from zoo order by count")
rows = curs.fetchall()
print(rows)

# close
curs.close()
conn.close()
