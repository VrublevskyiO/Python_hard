import csv
import psycopg2

username = 'postgres'
password = 'karysel55'
database = 'Second_lab'
host = 'localhost'
port = '5432'

OUTPUT_FILE_T = 'Lab_DB.csv'

TABLES = [
    'Population',
    'Region',
    'Time_series_info',
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])