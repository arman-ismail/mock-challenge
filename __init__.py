
from psycopg2 import pool


try:
    connection_pool = pool.SimpleConnectionPool(
        1,
        20,
        dbname="concerts",
        user="abdirahman",
        password="37571598a",
        host="localhost",
        port="5432",
    )

    if connection_pool:
        print("Connection pool created successfully")
except Exception as e:
    print(f"Error creating connection pool: {e}")


def get_connection():
    """
    Retrieves a connection from the connection pool.
    Raises an error if no connection is available.
    """
    try:
        connection = connection_pool.getconn()
        if connection:
            print("Successfully retrieved a connection from the pool")
            return connection
        else:
            raise Exception("Failed to retrieve connection from pool")
    except Exception as e:
        print(f"Error getting connection: {e}")
        raise e


def close_connection(connection):
    """
    Returns a connection to the pool.
    """
    try:
        connection_pool.putconn(connection)
        print("Connection returned to the pool")
    except Exception as e:
        print(f"Error returning connection: {e}")
