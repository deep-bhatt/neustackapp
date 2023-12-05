from flask import Flask

from routes.cart import cart_routes
from routes.admin import admin_routes

from models.cart import CartManager

app = Flask(__name__)

cart_manager = CartManager()
cart_routes(app, cart_manager)
admin_routes(app, cart_manager)

if __name__ == "__main__":
  app.run(debug=True)
