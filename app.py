from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for store management
stores = [
    {"id": 1, "name": "Store 1", "location": "Mall X", "contact": "123-456-7890", "inventory": [
        {"product_name": "Product A", "stock_level": 100},
        {"product_name": "Product B", "stock_level": 204}
    ]},
    {"id": 2, "name": "Store 2", "location": "Mall Y", "contact": "987-654-3210", "inventory": [
        {"product_name": "Product C", "stock_level": 157},
        {"product_name": "Product D", "stock_level": 205}
    ]}
]

next_store_id = 3
sales_history = []
customers = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/store')
def store_management():
    return render_template('store.html', stores=stores)

@app.route('/add_store', methods=['POST', 'GET'])
def add_store():
    global next_store_id
    name = request.form.get('name')
    location = request.form.get('location')
    contact = request.form.get('contact')
    
    new_store = {"id": next_store_id, "name": name, "location": location, "contact": contact, "inventory": []}
    stores.append(new_store)
    next_store_id += 1
    
    return redirect(url_for('store_management'))

@app.route('/update_store/<int:store_id>', methods=['POST'])
def update_store(store_id):
    name = request.form.get('name')
    location = request.form.get('location')
    contact = request.form.get('contact')
    
    for store in stores:
        if store['id'] == store_id:
            store['name'] = name
            store['location'] = location
            store['contact'] = contact
            break
    
    return redirect(url_for('store_management'))

@app.route('/delete_store/<int:store_id>')
def delete_store(store_id):
    global stores
    stores = [store for store in stores if store['id'] != store_id]
    return redirect(url_for('store_management'))

@app.route('/inventory/<int:store_id>', methods=['GET', 'POST'])
def inventory(store_id):
    store = next((store for store in stores if store['id'] == store_id), None)
    if store is None:
        return "Store not found", 404

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        stock_level = int(request.form.get('stock_level'))
        restock_amount = int(request.form.get('restock_amount'))

        store['inventory'].append({"product_name": product_name, "stock_level": stock_level})
        return redirect(url_for('inventory', store_id=store_id))

    return render_template('inventory.html', store=store)

@app.route('/sell/<int:store_id>', methods=['GET', 'POST'])
def sell(store_id):
    store = next((store for store in stores if store['id'] == store_id), None)
    if store is None:
        return "Store not found", 404

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        quantity = int(request.form.get('quantity'))
        
        for item in store['inventory']:
            if item['product_name'] == product_name:
                if item['stock_level'] >= quantity:
                    item['stock_level'] -= quantity
                    sales_history.append({"store_id": store_id, "product_name": product_name, "quantity": quantity})
                    return redirect(url_for('sell', store_id=store_id))
                else:
                    return "Insufficient stock", 400

        return "Product not found", 404

    return render_template('sell.html', store=store)

@app.route('/sales_history')
def view_sales_history():
    return render_template('sales_history.html', sales_history=sales_history)

@app.route('/customers')
def view_customers():
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['POST', 'GET'])
def add_customer():
    if request.method == 'POST':
        name = request.form.get('name')
        contact = request.form.get('contact')
        customers.append({"name": name, "contact": contact, "purchase_history": [], "loyalty_points": 0})
        return redirect(url_for('view_customers'))

    return render_template('add_customer.html')



if __name__ == '__main__':
    app.run(debug=True)
