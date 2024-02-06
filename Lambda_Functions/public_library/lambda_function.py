import psycopg2
import json
import os
import boto3

def handler(event, context):
    a = get_public_audio()

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

def get_public_audio():
    conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            sslmode='require'
        )

    cur = conn.cursor()

    cur.execute("SELECT * FROM audio WHERE private=0")

    rows = cur.fetchall()

    audio_public = []
    for row in rows:
        audio_dict = {'id': row[0], 'uid': row[1], 'key': row[2], 'private': row[3],
                      'name': row[4], 'genre': row[5], 'duration': row[6]}
        audio_public.append(audio_dict)

    conn.close()

    return audio_public

