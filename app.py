from flask import Flask

from routes.cart import cart_routes
from routes.admin import admin_routes

from models.models import CartManager

app = Flask(__name__)

# Global cart. Assuming there's just one user using the server.
# To support more than one user, we'll need to manage user sessions.
cart_manager = CartManager()
cart_routes(app, cart_manager)
admin_routes(app)

if __name__ == "__main__":
  app.run(debug=True)
