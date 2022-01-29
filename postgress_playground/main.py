import psycopg2
import pandas as pd
from sqlalchemy import create_engine

#* To Start Service, Run:
# brew services start postgresql
#* To Stop Service, Run:
# brew services stop postgresql


DB_NAME = 'testdb'
DB_USER = 'test'
DB_PASSWORD = '123456'
DB_SERVER = '127.0.0.1'

connection = None
try:
    connection = psycopg2.connect(
        database=DB_NAME, 
        user=DB_USER, 
        password=DB_PASSWORD, 
        host=DB_SERVER, 
        port='5432')
    cursor = connection.cursor()

    #* Print postgres properties
    print(connection.get_dsn_parameters(), '\n')

    #* Print postgres version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f'Connected to - {record}', '\n')

    #* To use Pandas with PostgreSQL:
    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}')
    print(engine)

    #! For smaller data sets - Load all at once
        #! -------------------------------------------------------------
    #* Obtain DB data:
    df = pd.read_csv('./CADHKD-2021-15Min-py.csv', index_col=False)
    print(df.head(2))

    #* Save Pandas DF to PostgreSQL table:
    df.to_sql('cadhkd15min', engine, if_exists='replace', index=False)

    cadhkd15min_record_count = pd.read_sql_query('select count(*) from cadhkd15min', engine)
    print(cadhkd15min_record_count)

    #! For large data sets - Load data in chunks
        #! -------------------------------------------------------------
    for chunk in pd.read_csv('./CADHKD-2021-15Min-py.csv', index_col=False, chunksize=2000):
        chunk.to_sql('cadhkd15min', engine, if_exists='append', index=False)

    cadhkd15min_record_count = pd.read_sql_query('select count(*) from cadhkd15min', engine)
    print(cadhkd15min_record_count)

    #* Query the DB catalog:
    db_catalog = pd.read_sql_query('''select ordinal_position, column_name, data_type
                                    from information_schema.columns
                                    where table_name = 'cadhkd15min'
                                ''', engine).head()
    print(db_catalog)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to postgres", error)
finally:
    #* Close database connection
    if(connection):
        cursor.close()
        connection.close()
        print("Postgres connection is closed")