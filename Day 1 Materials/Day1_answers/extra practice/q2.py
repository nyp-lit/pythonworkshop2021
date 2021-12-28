
price = float(input("Enter videotape price: "))
copy = float(input("Enter number of videotapes purchased: "))
subtotal = price * copy
gst = subtotal * 0.07
total = subtotal + gst

print(f"Subtotal: ${subtotal:.2f}")
print(f"GST: ${gst:.2f}")
print(f"Total Amount: ${total:.2f}")
