
#* To Start Service:
# brew services start postgresql
#* To Stop Service:
# brew services stop postgresql

import psycopg2


connection = None
try:
    connection = psycopg2.connect(
        database="testdb", 
        user="test", 
        password="12345", 
        host="127.0.0.1", 
        port="5432")
    cursor = connection.cursor()

    #* Print postgres properties
    print(connection.get_dsn_parameters(), '\n')

    #* Print postgres version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f'Connected to - {record}', '\n')

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to postgres", error)
finally:
    #* Close database connection
    if(connection):
        cursor.close()
        connection.close()
        print("Postgres connection is closed")