import jwt, datetime
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from app import settings
from core.models import User


class JWTAuthentication:

    @staticmethod
    def generate_jwt(id):
        payload = {
            'user_id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')