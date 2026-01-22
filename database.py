import mysql.connector as sql
from data import entry
conn=sql.connect(host="localhost",user="root",password="root")
cur=conn.cursor()
cur.execute("use healthcheck ;")
def getData():
    entries=[]
    cur.execute("select * from entries")
    data =cur.fetchall()
    for i in data:
        entries.append(entry(s_no=i[0],age=i[1],weight=i[2],height=i[3]))
    return entries
def add_data(entry:entry):
    query=f"insert into entries (age, weight, height) values \
        ({entry.age},{entry.weight},{entry.height});"
    cur.execute(query)
    return "whoooo added broooo"
def update_data(s_no:int,entry:entry):
    query=f"update entries set age={entry.age}weight={entry.weight},height={entry.height};"
    cur.execute(query)
    return "updated successfully"
def del_data(s_no:int):
    query=f"delete from entries where s_no={s_no}"
    cur.execute(query)
    return "done"