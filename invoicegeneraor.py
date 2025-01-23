def generate_invoice():
    print("Welcome to the Invoice Generator")

    # Get user input
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    item_description = input("Enter item description: ")
    item_quantity = int(input("Enter item quantity: "))
    item_price = float(input("Enter item price: "))

    # Calculate total
    total = item_quantity * item_price

    # Generate invoice
    invoice = f"""
    Invoice
    --------
    Customer Name: {customer_name}
    Customer Address: {customer_address}

    Item Description: {item_description}
    Item Quantity: {item_quantity}
    Item Price: ${item_price:.2f}

    Total: ${total:.2f}
    """

    print(invoice)

if __name__ == "__main__":
    generate_invoice()