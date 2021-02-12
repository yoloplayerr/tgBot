import pandas as pd
from queries import list2
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df=pd.DataFrame(list2,columns=['Жанр','Автор','Книга'])
#print(tabulate(df,headers='keys',tablefmt='psql'))
#print(df.value_counts())


fig = plt.figure()
#ax_1 = fig.add_subplot(4, 4, 1)
#ax_2 = fig.add_subplot(4, 4, 2)
#ax_3 = fig.add_subplot(4, 4, 3)

#
#plt.bar(df.value_counts(),df['book'])
#print(type(df.value_counts()))
df['CountsAuthor']=df.groupby(['Автор'])['Жанр'].transform('count')
df['CountsBook']=df.groupby(['Книга'])['Жанр'].transform('count')
df['CountsGenre']=df.groupby(['Жанр'])['Жанр'].transform('count')
print(tabulate(df,headers='keys',tablefmt='psql'))

plt.barh(df['Книга'],df['CountsBook'])

#print((df['book'].where(df['genre']=='Ужасы').dropna()))
#plt.legend()
plt.show()
