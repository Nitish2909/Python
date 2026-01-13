import qrcode

upi_id = input("Enter your UPI ID :")   

# upi Payment url format:
# upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY
"""
pa = payee address(upi id)
pn = payee name
am = amount
cu = currency(INR)
"""

# defining the payment url based on the UPI ID and Payment app
upiapp_url= f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Create QR Code for each Payment app
upiapp_qr = qrcode.make(upiapp_url)


# Save QR Code to image file(optional)
upiapp_qr.save("upiapp.png")


# DisPlay QR Code 
upiapp_qr.show()

