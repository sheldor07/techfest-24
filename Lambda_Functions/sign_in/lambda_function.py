import psycopg2

import psycopg2
import json
import secrets
import os

def handler(event, context):

    if 'body' not in event:
        return { "statusCode": 400, "body": json.dumps("Bad request") }

    connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            sslmode='require'
        )
    cursor = connection.cursor()

    # Retrieve user data from the request body
    body = json.loads(event['body'])

    if 'email' not in body or 'password' not in body:
        return { "statusCode": 400, "body": json.dumps("Bad request") }

    email = body['email']
    password = body['password']

    # Check if the email and password exist in the "user" table
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    if user is None:
        return { "statusCode": 400, "body": json.dumps("Invalid credentials") }

    uid = user[0]  # Assuming the uid is the first column of the user table
    token = secrets.token_hex(256)

    # Insert the uid and token into the "current_sign_in" table
    cursor.execute("INSERT INTO current_sign_in (uid, token) VALUES (%s, %s)", (uid, token))
    connection.commit()

    # Close the connection and the cursor
    cursor.close()
    connection.close()

    return { "statusCode": 200, "body": json.dumps({ "token": token }) }