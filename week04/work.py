import pandas as pd
import numpy as np

sql  =  ['SELECT * FROM data;',
        'SELECT * FROM data LIMIT 10;',
        'SELECT id FROM data;  //id 是 data 表的特定一列',
        'SELECT COUNT(id) FROM data;',
        'SELECT * FROM data WHERE id<1000 AND age>30;',
        'SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;',
        'SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;',
        'SELECT * FROM table1 UNION SELECT * FROM table2;',
        'DELETE FROM table1 WHERE id=10;',
        'ALTER TABLE table1 DROP COLUMN column_name;'
        ]

data = pd.DataFrame({
    'id':range(1,21),
    'salary':np.random.randint(5000,10000,20),
    'age':np.random.randint(15,50,20)
    })

table1 = pd.DataFrame({
    'id':np.arange(1,12),
    'age':np.random.randint(15,50,11)
})
table2 = pd.DataFrame({
    'id':np.arange(1,6),
    'salary':np.random.randint(4000,8000,5)
})
# print(table1)
# print(table2)

print("SQL 1:" + sql[0])
print(data)    

print("SQL 2:" + sql[1])
print(data.head(10))

print("SQL 3:" + sql[2])
print(data['id'])

print("SQL 4:" + sql[3])
print(data['id'].count())

print("SQL 5:" + sql[4])
df5 = data[(data['id']<1000) & (data['age']>30)]
print(df5)

print("SQL 6:" + sql[5])
df6 = table1.groupby('id')['order_id'].nunique()
print(df6)

print("SQL 7:" + sql[6])
df7 = pd.merge(table1, table2, on ='id', how ='inner')
print(df7)

print("SQL 8:" + sql[7])
df8 = pd.concat([table1, table2])
print(df8)

print("SQL 9:" + sql[8])
df9 = table1.drop(9 ,axis = 0)
print(df9)

print("SQL 10:" + sql[9])
df10 = table1.drop('age',axis = 1)
print(df10)