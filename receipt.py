from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_receipt_pdf(filename, transaction_info):
    # Create a canvas
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Draw the header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(1 * inch, height - 1 * inch, "Payment Receipt")
    
    # Draw the transaction details
    c.setFont("Helvetica", 12)
    text = f"""
    Date: {transaction_info['date']}
    Receipt No: {transaction_info['receipt_no']}
    
    Customer Name: {transaction_info['customer_name']}
    Items Purchased:
    """
    
    c.drawString(1 * inch, height - 1.5 * inch, text)
    
    y_position = height - 2 * inch
    for item, price in transaction_info['items'].items():
        c.drawString(1.2 * inch, y_position, f"{item}: ${price}")
        y_position -= 0.25 * inch
    
    # Total Amount
    total_amount = sum(transaction_info['items'].values())
    c.drawString(1 * inch, y_position - 0.5 * inch, f"Total Amount: ${total_amount}")
    
    # Draw the footer
    c.drawString(1 * inch, y_position - 1 * inch, "Thank you for your purchase!")
    
    # Save the PDF
    c.save()

# Example usage
transaction_info = {
    'date': '2024-08-13',
    'receipt_no': '12345',
    'customer_name': 'John Doe',
    'items': {
        'Item 1': 29.99,
        'Item 2': 49.99,
        'Item 3': 19.99
    }
}

create_receipt_pdf("receipt.pdf", transaction_info)
