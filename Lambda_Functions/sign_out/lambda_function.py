import psycopg2
import json
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

    if 'token' not in body:
        return { "statusCode": 400, "body": json.dumps("Bad request") }
    
    token = body['token']

    # delete record from current_sign_in where token = token
    cursor.execute(f"DELETE FROM current_sign_in WHERE token = '{token}'")

    connection.commit()
    cursor.close()
    connection.close()

    return {
        "statusCode": 200,
        "body": json.dumps("Logged out successfully")
    }
