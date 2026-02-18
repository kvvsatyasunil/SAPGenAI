from utils.reuse import print_products, calculate_price_with_gst
import utils.reuse as reuse

#Create list of products with their details price, quantity, category, and rating
products = [
    {"name": "Laptop", "price": 999.99, "quantity": 10, "category": "Electronics", "rating": 4.5},
    {"name": "Smartphone", "price": 499.99, "quantity": 20, "category": "Electronics", "rating": 4.7},
    {"name": "Headphones", "price": 199.99, "quantity": 15, "category": "Electronics", "rating": 4.3}, 
    {"name": "Coffee Maker", "price": 79.99, "quantity": 5, "category": "Home Appliances", "rating": 4.0},
    {"name": "Blender", "price": 59.99, "quantity": 8, "category": "Home Appliances", "rating": 4.2},
    {"name": "Banana", "price": 1.99, "quantity": 50, "category": "Fruits", "rating": 4.6},
    {"name": "Apple", "price": 2.49, "quantity": 40, "category": "Fruits", "rating": 4.8},
    {"name": "Carrot", "price": 0.99, "quantity": 60, "category": "Vegetables", "rating": 4.4},
    {"name": "Broccoli", "price": 3.99, "quantity": 25, "category": "Vegetables", "rating": 4.5}
]


#print the products and their details
print_products(products)



calculate_price_with_gst(products[0])
reuse.calculate_price_with_gst(products[0])