import requests
import json
import numpy as np
import boto3
import time
import random
import string
import hashlib
from scipy.io.wavfile import write
import os
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()

def generate_audio(prompt, duration=20):
    
    API_URL = os.getenv("API_URL")
    
    headers = {
        "Accept" : "application/json",
        "Authorization": "Bearer " + os.getenv("HF_TOKEN"),
        "Content-Type": "application/json" 
    }
    payload = {
        "inputs": prompt,
        "parameters": {}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return {
            "statusCode": 500,
            "body" : json.dumps({"error": "Music Gen Error 1"})
        }
    output = response.json()

    try:
        float_data = output[0]["generated_audio"][0]
    except:
        return {
            "statusCode": 500,
            "body" : json.dumps({"error": "Music Gen Error 2"})
        }

    numpy_data = np.array(float_data)
    numpy_data *= 32767
    numpy_data = numpy_data.astype(np.int16)
    key = generate_unique_key()

    filepath = "/tmp/" + key + ".wav"
    s3key = key + ".wav"

    write(filepath,  data=numpy_data, rate=32000)

    overwrite_first_n_seconds(filepath, duration)

    saveToS3(filepath, s3key)

    # os.remove("/tmp/" + key+".wav")

    return key

def saveToS3(file_name, filekey):
    
    s3 = boto3.client("s3", aws_access_key_id=os.getenv("AWS_ACCESS_KEY"), aws_secret_access_key=os.getenv("AWS_SECRET_KEY"), region_name=os.getenv("AWS_REGION"))
    s3.upload_file(file_name, os.getenv("S3_BUCKET"), filekey)
        
def generate_unique_key():
    timestamp = round(time.time() * 1000)
    random_str = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 16))
    full_str = str(timestamp) + random_str
    hash_object = hashlib.sha1(full_str.encode())
    hex_dig = hash_object.hexdigest() 

    return hex_dig

def generate_name(prompt):
    
    url = os.getenv("NAME_API_URL")
    headers = {
        "x-api-key": os.getenv("NAME_API_KEY"),
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt
    }

    res = requests.post(url, headers=headers, json=data)
    return res.json()["name"]

def generate_genre(prompt):
    
    url = os.getenv("GENRE_API_URL")
    headers = {
        "x-api-key": os.getenv("GENRE_API_KEY"),
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt
    }

    res = requests.post(url, headers=headers, json=data)
    return res.json()["name"]

def get_url(s3key):
    
    s3 = boto3.client("s3", aws_access_key_id=os.getenv("AWS_ACCESS_KEY"), aws_secret_access_key=os.getenv("AWS_SECRET_KEY"), region_name=os.getenv("AWS_REGION"))
    return s3.generate_presigned_url("get_object", Params={"Bucket": os.getenv("S3_BUCKET"), "Key": s3key}, ExpiresIn=36000)

def generate_prompt(prompt, genre):
    
    url = os.getenv("PROMPT_API_URL")
    headers = {
        "x-api-key": os.getenv("PROMPT_API_KEY")
    }

    r = requests.post(url, headers=headers, json={"prompt": prompt, "genre": genre})
    return r.json()["prompt"]

def overwrite_first_n_seconds(file_path, duration_in_seconds):
    audio = AudioSegment.from_wav(file_path)
    n_seconds = duration_in_seconds * 1000
    first_n_seconds = audio[:n_seconds]
    first_n_seconds.export(file_path, format="wav")
