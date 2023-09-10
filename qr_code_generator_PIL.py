# Import necessary libraries
import qrcode
from PIL import Image

# Author: Preet Kumarr
# Description: This script generates a customized QR code image using the qrcode library and saves it to a specified file.
# It allows customization of the data to be encoded and the output filename.

# Function to generate a customized QR code
def generate_customized_qr_code(data, output_filename):
    # Create a QRCode object with custom settings
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    # Add data to the QRCode
    qr_code.add_data(data)
    qr_code.make(fit=True)

    # Create the QRCode image with custom fill and background colors
    img = qr_code.make_image(fill_color='purple', back_color='black')

    # Save the customized QRCode to the specified output filename
    img.save(output_filename)

if __name__ == "__main__":
    # Specify the data to encode and the output filename
    data_to_encode = 'Preet Rathi'
    output_file = 'customized_qr.png'
    
    # Generate and save the customized QR code
    generate_customized_qr_code(data_to_encode, output_file)
    
    # Print a message indicating the successful save
    print(f"Customized QR code saved as '{output_file}'")
