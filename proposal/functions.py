from django.conf import settings
import requests
import os


if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Replace with your project name
    import django
    django.setup()

def send_whatsapp_message(phone_number, message):
    """
    Send a WhatsApp message using the WhatsApp Business API.

    Args:
        phone_number (str): The recipient's phone number, including country code.
        message (str): The text message to send.

    Returns:
        dict: The JSON response from the API or an error message if the request fails.
    """
    # Validate that required settings are available
    if not hasattr(settings, 'WHATSAPP_TOKEN') or not hasattr(settings, 'WHATSAPP_URL'):
        raise ValueError("WHATSAPP_TOKEN and WHATSAPP_URL must be defined in Django settings.")

    # Set headers
    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }

    # Define payload
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_number,
        "type": "text",
        "text": {"body": message},
    }

    try:
        # Make the POST request
        response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)

        # Check if the response is successful
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Failed to send message. Status code: {response.status_code}",
                "details": response.json() if response.headers.get("Content-Type") == "application/json" else response.text,
            }
    except requests.exceptions.RequestException as e:
        # Handle exceptions during the request
        return {"error": "An error occurred while sending the message", "details": str(e)}


response = send_whatsapp_message("2349125442676", "Hello, this is a test message.")
print(response)