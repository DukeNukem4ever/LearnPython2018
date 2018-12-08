import sqlite3

# подключаемся к базе данных
conn = sqlite3.connect('corpus2.db')

# создаем объект "курсор", которому будем передавать запросы
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS nanai')

# создаем таблицу

#c.execute("CREATE TABLE IF NOT EXISTS vowels (dictor text, sex text, village text, sound text, f1 integer, f2 integer)")

# вставляем строку

#c.execute("INSERT INTO vowels VALUES ('and','m',''Dzhuen'','i',343.936473,2087.688061)")#, ('Маша Петрова','история',4)")
#x = ('and',)
#c.execute('SELECT * FROM vowels WHERE dictor=?',x)
#print(c.fetchone())

params = ['dictor','sex','village','sound','f1','f2']
c.execute('CREATE TABLE nanai({},{},{},{},{},{})'.format(params[0],params[1],params[2],params[3],params[4],params[5]))
c.execute('''
INSERT INTO nanai 
VALUES 
('and','m','Dzhuen','i',343.936473,2087.688061),
('and','m','Dzhuen','i',376.343722,1939.472803),
('and','m','Dzhuen','i',253.490671,1094.884894),
('and','m','Dzhuen','i',276.426595,2314.701435),
('and','m','Dzhuen','i',325.202525,1987.125705),
('and','m','Dzhuen','i',299.584186,2499.441434),
('and','m','Dzhuen','i',244.041092,2428.071499),
('and','m','Dzhuen','i',347.245943,2498.858329),
('and','m','Dzhuen','i',332.798430,2600.633322),
('and','m','Dzhuen','i',320.204854,1915.155883),
('and','m','Dzhuen','i',317.000040,1918.849423),
('and','m','Dzhuen','i',330.576415,2013.858349),
('and','m','Dzhuen','i',369.762741,2099.704555),
('and','m','Dzhuen','i',269.531831,2083.978450),
('and','m','Dzhuen','i',272.483199,2197.627238),
('and','m','Dzhuen','i',273.694923,2104.989996),
('and','m','Dzhuen','i',281.424213,2071.745581),
('and','m','Dzhuen','i',279.258095,2103.560414),
('and','m','Dzhuen','i',280.218230,2147.794598),
('and','m','Dzhuen','i',282.944723,2127.743673),
('and','m','Dzhuen','i',272.443751,2097.994161),
('and','m','Dzhuen','i',262.031789,2089.603532),
('and','m','Dzhuen','i',254.885560,2101.125727)
'''
          )
#('u', 1111.1, 3333.3)'''

c.execute('SELECT * FROM nanai ORDER BY village')
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())

# сохраняем изменения
conn.commit()

# отключаемся от БД
#conn.close()
