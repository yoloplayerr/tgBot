from aiogram import Bot, types
from DBConnection import con,cur
from main import dp
from tabulate import tabulate
import pandas as pd
'''
def log():
 cur.execut
 con.commit()
'''

list1=[]
list2=[]
cur.execute("select * from logirovanie")
rows = cur.fetchall()
 #for i in rows:
    # print(i)

con.commit()
for i in rows:
 i1=list(i)
 list1.append(i1)

for i in list1:
    del i[0]
    list2.append(i)
#df=pd.DataFrame(list1)
#print(df)
#df.to_csv('fromdb')
#print(tabulate(df,headers='keys',tablefmt='psql'))
#print(df)
