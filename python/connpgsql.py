import psycopg2

try:
    conn = psycopg2.connect("dbname='exam' user='postgres' host='localhost' password='1234' port='5432'")
    curs = conn.cursor()
    sql_string = "select * from address"
    curs.execute(sql_string)
    result = curs.fetchall()
    print(result)
    conn.commit()
except:
    print("I am unable to connect to the database")
