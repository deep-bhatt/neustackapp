# Deep Bhatt
# Hiring Task - UniBlox

## Neustackapp

Neustackapp is an e-commerce application that allows users to add products to their cart, and proceed to checkout. The cart also gives out a 10% off discount code on every nth order. The app also contains an Admin API which can be used to fetch statistics such as count of items purchased, total purchase amount, list of discount codes and total discount amount.

The project uses Python3 and Flask web-framework.

## 💻 How to run

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the project requirements.

```bash
# Clone the repo
* git clone https://github.com/deep-bhatt/neustackapp.git
* cd ./neustackapp

# Installs project dependencies
* pip -r install requirements.txt

# Starts the development server on http://127.0.0.1:5000
* flask run
```

## 📁 File Structure

* `/models` contains data object definition for Item, Cart and Order.<br><br>
* `/services` contains helper functions for facilitating discounts.<br><br>
* `/store` contains application in-memory global state, this is an alternative way of achieving Singleton behavior. It also contains getters and setters for managing the global state.<br><br>
* `/tests` contains unit-tests that thoroughly tests adding to cart, checkout and discount functionality, it also tests getters and setters methods for global state.<br><br>

## 🔩 Running unit tests
```bash
# This runs all unitests defined in /tests directory
python -m unitest
```

## 🔨 Running API tests ( using Postman )

* The repository contains a Postman Collection file, which can be imported in Postman.<br><br>
* It should contain a `TESTS` directory. Which contains API tests.<br><br>
* API test first resets the application state, and then tests the APIs for correctness.<br><br>

![Postman API Tests](/docs/postman-collection.png)

## ✍️ Developer Notes
* Every nth order gets a coupon code for 10% discount and can apply to their cart. Here, the value of `N` is defined in `/store/stats.py`. <br><br>
* The application support multiple users by setting a HTTP header `x-user-id` in the reqeusts to APIs. This just for demonstration purposes and not meant for actual use. <br><br>
* The endpoint `POST /reset` resets application gobal state and order statistics. This was done to run API tests without inducing side effects.

## License
[MIT](https://choosealicense.com/licenses/mit/)
