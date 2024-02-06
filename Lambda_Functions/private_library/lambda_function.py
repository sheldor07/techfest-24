import psycopg2
import json
import boto3
import os

def handler(event, context):

    if 'body' not in event:
        return {
            "statusCode": 400,
            "body": json.dumps("Invalid request")
        }
    
    body = json.loads(event['body'])

    if 'token' not in body:
        return {
            "statusCode": 400,
            "body": json.dumps("Invalid request")
        }
    
    token = body['token']

    uid = get_uid(token)

    if not uid:
        return {
            "statusCode": 401,
            "body": json.dumps("Unauthorized")
        }

    a = get_private_audio(uid)

    key = os.getenv("AWS_ACCESS")
    secret = os.getenv("AWS_SECRET")

    s3 = boto3.client("s3", aws_access_key_id=key, aws_secret_access_key=secret, region_name="ap-south-1")
    newlist = []
    for audio in a:
        s3key = audio['key'] + ".wav"
        s3url = s3.generate_presigned_url('get_object', Params={'Bucket': 'techfest-mp3', 'Key': s3key}, ExpiresIn=3600)
        audio['url'] = s3url
        newlist.append(audio)

    return {
        "statusCode": 200,
        "body": json.dumps(newlist)
    }

def get_private_audio(uid):
    conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            sslmode='require'
        )

    cur = conn.cursor()

    cur.execute("SELECT * FROM audio WHERE uid=%s", (uid,))

    rows = cur.fetchall()

    audio_public = []
    for row in rows:
        audio_dict = {'id': row[0], 'uid': row[1], 'key': row[2], 'private': row[3],
                      'name': row[4], 'genre': row[5], 'duration': row[6]}
        audio_public.append(audio_dict)

    conn.close()

    return audio_public


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
