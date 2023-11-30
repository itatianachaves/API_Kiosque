
from menu import products

def calculate_tab(consumption):
    subtotal = 0
    for product in products:
        for expense in consumption:
            if product["_id"] == expense["_id"]:

                subtotal = subtotal + product["price"] * expense["amount"]
   
    return {"subtotal": f"${round(subtotal,2)}"}
