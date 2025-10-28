from ninja import NinjaAPI

from api.auth.endpoints import auth_router
from api.utils import AdminApiKey, ApiKey

header_key = ApiKey()
admin_header_key = AdminApiKey()

#Testing CI/CD

description = f"""
An API for the Educational Platform.

The auth works by checking if the provided `{header_key.param_name}` exists in the database.
"""

api = NinjaAPI(
    title="Product List API",
    version="1.0.0",
    description=description,
    auth=header_key,
)

api.add_router("/auth", auth_router, tags=["auth"])
