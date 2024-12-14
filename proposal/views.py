from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from .functions import *
import json
# Create your views here.

def home(request):
	return render(request, "proposal/index.html")

@csrf_exempt
def WhatsAppWebhook(request):
	if request.method == 'GET':
		VERIFY_TOKEN='a6b53efd-a6fe-4025-99e7-3f2f225fd049'
		mode= request.GET['hub.mode']
		token = request.GET['hub.verify_token']
		challenge = request.GET['hub.challenge']
		if mode == 'subscribe' and token == VERIFY_TOKEN:
			return HttpResponse(challenge, status=200)
		else:
			return HttpResponse('error', status=403)
	if request.method == 'POST':
		data = json.loads(request.body)
		return HttpResponse('success', status=200)
