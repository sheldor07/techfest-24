import psycopg2
import json
import os
import secrets

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

    # Check if the email already exists in the "user" table
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user is not None:
        return { "statusCode": 400, "body": json.dumps("Email already registered") }

    # Insert the email and password into the "user" table
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s) RETURNING uid", (email, password))
    uid = cursor.fetchone()[0]

    token = secrets.token_hex(128)

    # Insert the uid and token into the "current_sign_in" table
    cursor.execute("INSERT INTO current_sign_in (uid, token) VALUES (%s, %s)", (uid, token))
    connection.commit()

    # Close the connection and the cursor
    cursor.close()
    connection.close()

    return { "statusCode": 200, "body": json.dumps({ "uid": uid, "token": token }) }