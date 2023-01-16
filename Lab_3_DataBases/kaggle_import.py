import psycopg2

username = 'postgres'
password = 'karysel55'
database = 'Second_lab'
host = 'localhost'
port = '5432'



query_1 = '''
CREATE TABLE IF NOT EXISTS public."Population_new"
(
    region integer,
    date integer,
    gender "char",
    age text COLLATE pg_catalog."default",
    amount integer
)
'''

query_2 = '''
CREATE TABLE IF NOT EXISTS public."Region_new"
(
    code integer,
    name text COLLATE pg_catalog."default"
)
'''

query_3 = '''
CREATE TABLE IF NOT EXISTS public."Time_series_info_new"
(
    year integer NOT NULL,
    martality_rate real,
    mid_salary_uah real,
    "GDP" real,
    fertility_rate real,
    CONSTRAINT "Time_series_info_pkey" PRIMARY KEY (year)
)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

cur = conn.cursor()


with open('/Users/vrublevskyi.o/Downloads/Lab_2_Databases/Time_series/Population-population.csv', 'r') as f1:
    cur.execute('DROP TABLE public."Population_new"')
    cur.execute(query_1)
    next(f1)
    cur.copy_from(f1, 'public."Population_new"', sep=',')
conn.commit()

with open('/Users/vrublevskyi.o/Downloads/Lab_2_Databases/Time_series/Region-region_0.csv', 'r') as f2:
    cur.execute('DROP TABLE public."Region_new"')
    cur.execute(query_2)
    next(f2)
    cur.copy_from(f2, 'public."Region_new"', sep=',')
conn.commit()

with open('/Users/vrublevskyi.o/Downloads/Lab_2_Databases/Time_series/Time_series_info-Time_series_info.csv', 'r') as f3:
    cur.execute('DROP TABLE public."Time_series_info_new"')
    cur.execute(query_3)
    next(f3)
    cur.copy_from(f3, 'public."Time_series_info_new"', sep=',')
conn.commit()