from flask import Flask, render_template, redirect, url_for, request, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['jewellery']

# Define MongoDB collections
checkout_collection = db['checkout']
details_collection = db['details']
contact_collection = db['contact']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/product')
def product():
    # Static product data
    products = [
        {
            '_id': 'product_id_1',
            'name': 'Product 1 Name',
            'price': 12100,
            'image': '1.jpg'
        },
        {
            '_id': 'product_id_2',
            'name': 'Product 2 Name',
            'price': 32200,
            'image': '2.jpg'
        },
        {
            '_id': 'product_id_3',
            'name': 'Product 3 Name',
            'price': 45150,
            'image': '3.jpg'
        }
    ]

    cart_item_count = session.get('cart_item_count', 0)
    return render_template('product.html', products=products, cart_item_count=cart_item_count)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    if product_id:
        if 'cart' not in session:
            session['cart'] = {}
        
        cart = session['cart']
        # Find product in the static list instead of MongoDB
        products = [
            {
                '_id': 'product_id_1',
                'name': 'Product 1 Name',
                'price': 12100,
                'image': '1.jpg'
            },
            {
                '_id': 'product_id_2',
                'name': 'Product 2 Name',
                'price': 32200,
                'image': '2.jpg'
            },
            {
                '_id': 'product_id_3',
                'name': 'Product 3 Name',
                'price': 45150,
                'image': '3.jpg'
            }
        ]

        product = next((prod for prod in products if prod['_id'] == product_id), None)
        
        if product_id in cart:
            cart[product_id]['quantity'] += 1
        else:
            cart[product_id] = {
                'name': product['name'],
                'price': product['price'],
                'image': product['image'],
                'quantity': 1
            }
        
        session.modified = True
        session['cart'] = cart
        session['cart_item_count'] = len(cart)
    return redirect(url_for('cart'))

@app.route('/update_cart', methods=['POST'])
def update_cart():
    product_id = request.form.get('product_id')
    action = request.form.get('action')
    
    if 'cart' in session:
        cart = session['cart']
        if product_id in cart:
            if action == 'add':
                cart[product_id]['quantity'] += 1
            elif action == 'remove':
                cart[product_id]['quantity'] -= 1
                if cart[product_id]['quantity'] <= 0:
                    del cart[product_id]
        
        session.modified = True
        session['cart'] = cart
        session['cart_item_count'] = len(cart)
    
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    cart_items = []
    total_amount = 0
    
    # Static product data
    products = [
        {
            '_id': 'product_id_1',
            'name': 'Blue Stone Ring',
            'price': 12100,
            'image': '1.jpg'
        },
        {
            '_id': 'product_id_2',
            'name': 'Sapphire Ring',
            'price': 32200,
            'image': '2.jpg'
        },
        {
            '_id': 'product_id_3',
            'name': 'Earrings',
            'price': 150,
            'image': '13.jpg'
        }
    ]
    
    for product_id, item in cart.items():
        # Find product in the static list instead of MongoDB
        product = next((prod for prod in products if prod['_id'] == product_id), None)
        if product:
            item['image'] = product.get('image', 'default.jpg')  # Default image if not found
            item['total'] = item['price'] * item['quantity']
            total_amount += item['total']
            cart_items.append(item)
    
    cart_item_count = session.get('cart_item_count', 0)
    return render_template('cart.html', cart_items=cart_items, cart_item_count=cart_item_count, total_amount=total_amount)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        address = request.form.get('address')
        phone = request.form.get('phone')
        payment_name = request.form.get('payment_name')
        utr = request.form.get('utr')
        transaction_id = request.form.get('transaction')

        # Store checkout details in MongoDB
        try:
            checkout_collection.insert_one({
                'name': name,
                'email': email,
                'address': address,
                'phone': phone,
                'payment_name': payment_name,
                'utr': utr,
                'transaction_id': transaction_id
            })
            # Clear cart after successful checkout
            session.pop('cart', None)
            session.pop('cart_item_count', None)
            return redirect(url_for('payment_confirm'))  # Redirect to payment confirmation page
        except Exception as e:
            print(f"Error storing checkout data: {e}")
            # Optionally, handle the error and inform the user
            return "An error occurred. Please try again later."

    # Render the checkout form
    return render_template('checkout.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("POST request received")
        # Extract form data
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        message = request.form.get('message')
        email = request.form.get('email')
        address = request.form.get('address')
        contactnumber = request.form.get('contactnumber')
        
        try:
            # Store form data in the MongoDB collection
            contact_collection.insert_one({
                'firstname': firstname,
                'lastname': lastname,
                'message': message,
                'email': email,
                'address': address,
                'contactnumber': contactnumber
            })
            return redirect(url_for('contact_success'))  # Redirect to success page
        except Exception as e:
            print(f"Error storing contact data: {e}")
            # Optionally, handle the error and inform the user
            return "An error occurred. Please try again later."
        print("GET request received")
    # Render the contact form
    return render_template('contact.html')

@app.route('/contact_success')
def contact_success():
    return render_template('contact_success.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin_authenticate', methods=['POST'])
def admin_authenticate():
    # Get form data
    username = request.form['username']
    password = request.form['password']

    # Replace with your actual admin authentication logic
    if username == 'admin' and password == 'password':  # Simple check
        return redirect(url_for('admin_dashboard'))  # Redirect to admin dashboard
    else:
        return "Invalid login credentials, please try again."
    
@app.route('/logout', methods=['POST'])
def logout():
    # Clear session
    session.pop('cart', None)
    session.pop('cart_item_count', None)
    return redirect(url_for('home'))

@app.route('/admin_dashboard')
def admin_dashboard():
    # Fetch all booking data from the MongoDB collection
    bookings = checkout_collection.find()  # Use the correct collection

    # Fetch all user details from the MongoDB collection
    users = details_collection.find()

    contact_messages = contact_collection.find()

    # Pass the data to the admin dashboard template
    return render_template('admin_dashboard.html', bookings=bookings, users=users, contact_messages=contact_messages)

@app.route('/payment_confirm')
def payment_confirm():
    return render_template('payment_confirm.html')

if __name__ == '__main__':
    app.run(debug=True)
