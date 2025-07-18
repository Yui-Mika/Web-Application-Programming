from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = '123'  # used to encrypt sessions

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['Lab7']  # database name
product_collection = db['products']

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product = {
            "name": request.form["name"],
            "description": request.form["description"],
            "price": float(request.form["price"]),
            "image": request.form["image"]
        }
        product_collection.insert_one(product)
        return redirect(url_for('add_product'))  # After adding, reload the page
    return render_template('add_product.html')

# Display products
@app.route('/products')
def display_products():
    all_products = product_collection.find()
    return render_template('display_products.html', products=all_products)


# Edit product
@app.route('/edit-product/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = product_collection.find_one({'_id': ObjectId(product_id)})

    if request.method == 'POST':
        updated = {
            "name": request.form["name"],
            "description": request.form["description"],
            "price": float(request.form["price"]),
            "image": request.form["image"]
        }
        product_collection.update_one({"_id": ObjectId(product_id)}, {"$set": updated})
        return redirect(url_for('display_products'))

    return render_template('edit_product.html', product=product)


# Delete product
@app.route('/delete-product/<product_id>', methods=['POST'])
def delete_product(product_id):
    product_collection.delete_one({"_id": ObjectId(product_id)})
    return redirect(url_for('display_products'))

# Search products
@app.route('/search', methods=['GET'])
def search_product():
    query = request.args.get('query', '')
    if query:
        products = product_collection.find({"name": {"$regex": query, "$options": "i"}})
    else:
        products = []
    return render_template('search.html', products=products, query=query)


# Display shopping cart
@app.route('/cart')
def display_cart():
    cart = session.get('cart', [])
    total = sum(item['price'] * item.get('quantity', 1) for item in cart)
    return render_template('cart.html', cart=cart, total=total)


# Shopping cart
@app.route('/add-to-cart/<product_id>')
def add_to_cart(product_id):
    product = product_collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        return "Product not found", 404

    if 'cart' not in session:
        session['cart'] = []

    cart = session['cart']
    product_found = False

    # Check if product already exists then increase quantity
    for item in cart:
        if item['id'] == str(product['_id']):
            item['quantity'] += 1
            product_found = True
            break

    # If not, add new one
    if not product_found:
        cart.append({
            "id": str(product['_id']),
            "name": product['name'],
            "price": product['price'],
            "image": product['image'],
            "quantity": 1
        })

    session['cart'] = cart
    session.modified = True
    return redirect(url_for('display_cart'))




# update cart
@app.route('/update-quantity/<product_id>', methods=['POST'])
def update_quantity(product_id):
    action = request.form['action']
    cart = session.get('cart', [])

    for item in cart:
        if item['id'] == product_id:
            if action == 'increase':
                item['quantity'] += 1
            elif action == 'decrease' and item['quantity'] > 1:
                item['quantity'] -= 1
            break

    session['cart'] = cart
    session.modified = True
    return redirect(url_for('display_cart'))

# Remove item from cart
@app.route('/remove-item/<product_id>', methods=['POST'])
def remove_item(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    session.modified = True
    return redirect(url_for('display_cart'))


# Place order
@app.route('/place-order', methods=['POST'])
def place_order():
    cart = session.get('cart', [])
    
    if not cart:
        return "Cart is empty!", 400

    # Giả sử bạn có collection tên 'orders'
    orders = db['orders']
    orders.insert_one({
        "items": cart,
        "total": sum(item['price'] * item['quantity'] for item in cart)
    })

    # Clear cart
    session['cart'] = []
    session.modified = True

    # Go to notification page
    return render_template('order_success.html')



if __name__ == '__main__':
    app.run(debug=True)