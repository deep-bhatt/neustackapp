from flask import Flask

from routes.cart import cart_routes
from routes.admin import admin_routes

app = Flask(__name__)

cart_routes(app)
admin_routes(app)

if __name__ == "__main__":
  app.run(debug=True)
