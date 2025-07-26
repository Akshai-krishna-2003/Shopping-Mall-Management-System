# store_management.py

def add_store(stores, next_store_id, name, location, contact):      #to add a new store into our program
    new_store = {"id": next_store_id, "name": name, "location": location, "contact": contact, "inventory": []}
    stores.append(new_store)
    next_store_id += 1
    return stores, next_store_id

def sell_product(store, product_name, quantity):                    #selling and updating the program values
    for item in store['inventory']:
        if item['product_name'] == product_name:
            if item['stock_level'] >= quantity:
                item['stock_level'] -= quantity
                return store['inventory'], {"store_id": store['id'], "product_name": product_name, "quantity": quantity}
            else:
                return store['inventory'], None  # Return None to indicate insufficient stock
    return store['inventory'], None  # Return None to indicate product not found



def view_sales_history(sales_history):                              # lets us see history of sales transactions
    output = []
    for sale in sales_history:
        output.append(f"Store {sale['store_id']} - {sale['product_name']} (Quantity: {sale['quantity']})")
    return output

# Other sales management functions can be added here

