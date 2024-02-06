import psycopg2
import os
from dotenv import load_dotenv

def get_uid(token):
    try:
        # establish a connection
        
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            sslmode='require'
        )

        # create a cursor
        cursor = connection.cursor()

        # write your query
        query = "SELECT * FROM current_sign_in WHERE token = %s;"
        
        # execute the query
        cursor.execute(query, (token,))

        # fetch all the matching records
        records = cursor.fetchall()

        # close the cursor and the connection
        cursor.close()
        connection.close()

        # check if any record exists
        if records:
            return records[0][0]  # assuming uid column is the first one
        else:
            return False
            
    except (Exception, psycopg2.DatabaseError) as error:
        return False
    
    
def insert_audio(uid, key, name, genre, private, duration):
    try:
        
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            sslmode='require'
        )

        # create a cursor
        cursor = connection.cursor()

        # write your query
        query = "INSERT INTO audio (uid, key, name, genre, private, duration) VALUES (%s, %s, %s, %s, %s, %s);"

        # execute the query
        cursor.execute(query, (uid, key, name, genre, private, duration))

        # commit the changes
        connection.commit()

        # close the cursor and the connection
        cursor.close()
        connection.close()

        return True

    except (Exception, psycopg2.DatabaseError) as error:
        return False