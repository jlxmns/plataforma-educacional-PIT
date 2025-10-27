from ninja.security import APIKeyHeader

from api.models import AuthToken

# AUTH


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        try:
            token = AuthToken.objects.select_related("user").get(key=key)
            return token.user
        except AuthToken.DoesNotExist:
            return None


class AdminApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        try:
            token = AuthToken.objects.select_related("user").get(key=key)
            user = token.user
            if user.role == user.Role.ADMIN:
                return user
        except AuthToken.DoesNotExist:
            pass
        return None
