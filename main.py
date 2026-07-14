import qrcode
print('library installed successfully')

import qrcode

# Ask the user for a URL
url = input("Enter the website URL: ")

# Create the QR code
img = qrcode.make(url)

# Save the QR code image
img.save("website_qr.png")

print("QR Code generated successfully!")
print("Saved as website_qr.png")