from django.conf import settings
from django.http import JsonResponse
import requests


class Http403(Exception):
    pass


def success_response(**kwargs):
    message = kwargs.get("message", "ok")
    status = kwargs.get("status", 200)
    data = kwargs.get("data", {})

    return JsonResponse({"response": {"message": message, "data": data}}, status=status)


def error_response(**kwargs):
    status = kwargs.get("status", 400)
    errors = kwargs.get("errors", [])

    return JsonResponse({"response": {"errors": errors}}, status=status)


def mailgun_send_email(recipient, subject, html=None, tags=None):
    return requests.post(
        settings.MAILGUN_API_URI + "/messages",
        auth=("api", settings.MAILGUN_API_KEY),
        data={
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": [recipient],
            "subject": subject,
            "text": "Тестовое пиьсмо",
        }
    )
