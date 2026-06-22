"""
A E commence order Processing pipeline.
Here is an example, How to trace all of this with Traccia.
Just for demo purpose.

https://medium.com/@rudraprasadbhuyan999/tracing-an-e-commerce-order-processing-pipeline-with-traccia-38c7dca3d911
"""

import random
import time

from rich.pretty import pprint
from traccia import init, observe

# Print traces in terminal
init(enable_console_exporter=True)


@observe()
def validate_order(order):
    time.sleep(0.3)

    if order["quantity"] <= 0:
        raise ValueError("Quantity must be positive")

    return True


@observe()
def check_inventory(product_id, quantity):
    time.sleep(0.5)

    stock = random.randint(0, 20)

    return {
        "product_id": product_id,
        "requested": quantity,
        "available": stock,
        "in_stock": stock >= quantity,
    }


@observe()
def calculate_price(price, quantity):
    time.sleep(0.2)

    subtotal = price * quantity
    tax = subtotal * 0.18
    total = subtotal + tax

    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": total,
    }


@observe()
def process_payment(amount):
    time.sleep(1)

    payment_id = f"PAY-{random.randint(1000, 9999)}"

    return {
        "payment_id": payment_id,
        "amount": amount,
        "status": "SUCCESS",
    }


@observe()
def create_order(order):
    validate_order(order)

    inventory = check_inventory(order["product_id"], order["quantity"])

    if not inventory["in_stock"]:
        raise Exception(f"Only {inventory['available']} items available")

    pricing = calculate_price(order["price"], order["quantity"])

    payment = process_payment(pricing["total"])

    return {
        "order_id": f"ORD-{random.randint(10000, 99999)}",
        "inventory": inventory,
        "pricing": pricing,
        "payment": payment,
    }


if __name__ == "__main__":
    order = {
        "product_id": 101,
        "quantity": 2,
        "price": 1500,
    }

    try:
        result = create_order(order)
        pprint(result)

    except Exception as e:
        print("Error:", e)
