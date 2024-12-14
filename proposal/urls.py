from django.urls import path, include
from . import views

urlpatterns=[
	path('', wiews.home, name="home"),
	path('06f840f9-af3f-457f-a3a2-3705799b8fae', views.WhatsAppWebhook, name="whatsapp-webhook")
]

# https://wisteenbecca.onrender.com/06f840f9-af3f-457f-a3a2-3705799b8fae
# token: a6b53efd-a6fe-4025-99e7-3f2f225fd049