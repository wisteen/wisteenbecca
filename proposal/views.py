from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .functions import *
import json
import logging

# Configure logger
logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    return render(request, "proposal/index.html")

@csrf_exempt
def WhatsAppWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = 'a6b53efd-a6fe-4025-99e7-3f2f225fd049'
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')
        
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error', status=403)

    if request.method == 'POST':
        data = json.loads(request.body)
        logger.info(f"Incoming POST Data: {data}")
        print(data)
        if 'object' in data and 'entry' in data:
            try:
                for entry in data['entry']:
                    phoneNumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                    phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                    profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                    whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                    fromId = entry['changes'][0]['value']['messages'][0]['from']
                    messageId = entry['changes'][0]['value']['messages'][0]['id']
                    timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
                    text = entry['changes'][0]['value']['messages'][0]['body']
                    phoneNumber = "2349125442676"
                    message = 'RE: {} was received from wisteenbecca'.format(text)
                    logger.info(f"Processing message from {profileName}: {text}")

                    sendWhatsappMessage(phoneNumber, message)

            except:
                pass
                # logger.error(f"JSON decoding error: {e}")
                # return HttpResponse('Invalid JSON', status=400)

            # except Exception as e:
            #     logger.error(f"Error processing webhook: {e}")
            #     return HttpResponse('Error processing request', status=500)

    return HttpResponse('success', status=200)
