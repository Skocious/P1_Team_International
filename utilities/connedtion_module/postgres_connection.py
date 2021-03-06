from psycopg import connect, OperationalError
import os


def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASS"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        print(str(e))


connection = create_connection()

print(connection)
