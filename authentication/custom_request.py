from django.http import HttpRequest

from authentication.models import User


class AuthenticatedHttpRequest(HttpRequest):
    user: User
