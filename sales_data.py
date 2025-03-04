## Data sales for products, months ang quantity
sales_data = [
    {'product': 'Smartphone', 'month': 'January', 'quantity': 150},
    {'product': 'Laptop', 'month': 'January', 'quantity': 80},
    {'product': 'Tablet', 'month': 'January', 'quantity': 50},
    {'product': 'Smartphone', 'month': 'February', 'quantity': 200},
    {'product': 'Laptop', 'month': 'February', 'quantity': 90},
    {'product': 'Tablet', 'month': 'February', 'quantity': 60},
    {'product': 'Smartphone', 'month': 'March', 'quantity': 250},
    {'product': 'Laptop', 'month': 'March', 'quantity': 100},
    {'product': 'Tablet', 'month': 'March', 'quantity': 70},] 

product_sales = {}
month_sales = {}

def total_sales(sales_data):

    for entry in sales_data:
        product = entry["product"]
        month = entry["month"]
        quantity = entry["quantity"]
        
        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity
            
            
        if month in month_sales:
            month_sales[month] += quantity
        else:
            month_sales[month] = quantity