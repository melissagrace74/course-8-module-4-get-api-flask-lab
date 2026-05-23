from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"})


# GET /products (all products or filter by category)
@app.route("/products")
def get_products():
    category = request.args.get("category")

    if category:
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.lower()
        ]
        return jsonify(filtered_products)

    return jsonify(products)


# GET /products/<id> (single product or 404)
@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
    