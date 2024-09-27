from asgiref.wsgi import WsgiToAsgi
from app import app

# Wrap the Flask app with ASGIRefMiddleware
asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    # Use the ASGI app for running
    asgi_app.run(debug=True)