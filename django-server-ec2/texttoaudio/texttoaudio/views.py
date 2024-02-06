from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import requests
import psycopg2
from . import helpers
from . import db
import threading
import concurrent.futures
import os
from . import setenv

@csrf_exempt
def image(request):
    if request.method == 'POST':
        setenv.setenv()
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        
        token = body_data.get('token')
        image_data = body_data.get('image')
        duration = body_data.get('duration')
        private = body_data.get('private')

        if not token or not image_data or not duration or not private:
            return JsonResponse({"error": "Please provide all the required fields"})
        
        uid = db.get_uid(token)

        if not uid:
            return JsonResponse({"error": "Invalid token"})
        
        if private != 1 and private != 0:
            return JsonResponse({"error": "Invalid private value"})
        
        url = os.getenv('API_ENDPOINT')
        headers = {
            'x-api-key': os.getenv('API_KEY')
        }

        response = requests.post(url, headers=headers, data=image_data)
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(helpers.generate_name, response.text)
            future2 = executor.submit(helpers.generate_genre, response.text)
            future3 = executor.submit(helpers.generate_audio, response.text, duration)

        name = future1.result().replace("\"", "")
        genre = future2.result().replace("\"", "")
        key = future3.result()

        db.insert_audio(uid, key, name, genre, private, duration)
        url = helpers.get_url(key + ".wav")
        return JsonResponse({"status": "success", "key": key, "url": url})
    else:
        return JsonResponse({"error": "This endpoint only accepts POST requests"})

@csrf_exempt
def text(request):
    if request.method == 'POST':
        setenv.setenv()
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        
        token = body_data.get('token')
        prompt = body_data.get('prompt')
        genre = body_data.get('genre')
        duration = body_data.get('duration')
        private = body_data.get('private')

        if not token or not prompt or not genre or not duration or not private:
            return JsonResponse({"error": "Please provide all the required fields"})
        
        uid = db.get_uid(token)

        if not uid:
            return JsonResponse({"error": "Invalid token"})
        
        if private != 1 and private != 0:
            return JsonResponse({"error": "Invalid private value"})
        
        p = helpers.generate_prompt(prompt, genre)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(helpers.generate_name, p)
            future2 = executor.submit(helpers.generate_audio, p, duration)

        name = future1.result().replace("\"", "")
        key = future2.result()

        db.insert_audio(uid, key, name, genre, private, duration)

        url = helpers.get_url(key + ".wav")
        
        return JsonResponse({"status": "success", "key": key, "url": url})
    else:
        return JsonResponse({"error": "This endpoint only accepts POST requests"})