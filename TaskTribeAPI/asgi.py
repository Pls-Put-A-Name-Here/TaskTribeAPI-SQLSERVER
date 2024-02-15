import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import your_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskTribeAPI.settings')

# Django ASGI application
django_asgi_app = get_asgi_application()

# WebSocket routing
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            your_app.routing.websocket_urlpatterns
        )
    ),
})

