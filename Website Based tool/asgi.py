from asgiref.wsgi import WsgiToAsgi
from app import app
from contextlib import asynccontextmanager

# Wrap the Flask app with ASGIRefMiddleware
asgi_app = WsgiToAsgi(app)

@asynccontextmanager
async def lifespan(app):
    # Startup code here (if needed)
    yield
    # Shutdown code here (if needed)

# Create a new ASGI app with lifespan support
from starlette.applications import Starlette

app_with_lifespan = Starlette(lifespan=lifespan)
app_with_lifespan.mount("/", asgi_app)

if __name__ == '__main__':
    # Use the ASGI app for running
    asgi_app.run(debug=True)
