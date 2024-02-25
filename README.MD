# QR Code Generator in Python

This Python script generates a QR code from a user-provided link and saves it as an image.

**How to use:**

1. **Install the required library:**

   ```bash
   pip install qrcode

2. Save the script as a Python file (e.g., qr_code_generator.py)
3. Run the script:

    ```bash
    python qr_code_generator.py
    
4. Enter the link you want to encode into a QR code.
5. The script will prompt you repeatedly for links until you enter "q" to quit.

**The script will:**

- Ask for the URL you want to encode.
- Generate a QR code using the qrcode library.
- Set the error correction level for better resilience (optional).
- Save the QR code image as "qr_code.png" (with unique filename handling).
- Inform you about successful generation and the filename.

**Additional notes:**

- You can customize the generated QR code image by changing the box_size and border arguments in the create_qr_code function within the script (not exposed in the usage instructions).
- This script provides a basic implementation of QR code generation. You might explore various libraries like qrcode (alternative) and their functionalities for more advanced options.
