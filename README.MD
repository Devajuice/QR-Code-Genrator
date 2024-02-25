# QR Code Generator in Python

This Python script generates a QR code from a user-provided link and saves it as an image.

**Features:**

- Uses the `qrcode` library for QR code generation.
- Includes error correction for better resilience.
- Has a user-friendly interface for continuous link input.
- Generates unique filenames to avoid overwriting existing files.
- Provides informative error messages if issues arise.

**How to use:**

1. **Install the required library:**

   ```bash
   pip install qrcode
2. Save the script (***e.g., as qr_code_generator.py***)
3. Run the script:
    ```bash
    python yourfilename.py
    or 
    python3 yourfilename.py
4. Enter the link you want to encode **(or "q" to quit)**.
5. The script will generate and save the QR code image, providing success/error messages.

**Customization:**

Modify the `box_size` and border arguments in the `create_qr_code` function to adjust the appearance of the QR code.

**Additional notes:**

Explore the `qrcode` library's documentation for further customization options.
Consider using a virtual environment to manage project-specific dependencies. 