#generate the function to print the products and their details
def print_products(products):
    for product in products:
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']}")
        print(f"Quantity: {product['quantity']}")
        print(f"Category: {product['category']}")
        print(f"Rating: {product['rating']} stars")
        print("-" * 30)


def calculate_price_with_gst(product):
    gst_rates = {
        "Fruits": 0.12,
        "Dairy": 0.10,
        "Vegetables": 0.05,
        "Electronics": 0.20
    }
    
    category = product["category"]
    gst_rate = gst_rates.get(category, 0)
    gst_amount = product["price"] * gst_rate
    final_price = product["price"] + gst_amount
    
    print(f"{product['name']} ({category})")
    print(f"Original Price: ${product['price']:.2f}")
    print(f"GST ({gst_rate*100:.0f}%): ${gst_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")
    print("-" * 30)

if __name__ == "__main__":
    # Example usage
    products = [
        {"name": "Laptop", "price": 999.99, "quantity": 10, "category": "Electronics", "rating": 4.5},
        {"name": "Banana", "price": 1.99, "quantity": 50, "category": "Fruits", "rating": 4.6}
    ]
    
    print_products(products)
    calculate_price_with_gst(products[0])
    calculate_price_with_gst(products[1])