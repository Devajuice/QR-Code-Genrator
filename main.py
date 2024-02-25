import qrcode
import os

def create_qr_code(link, filename="qr_code.png", box_size=10, border=4):
    """
    Creates a QR code from a user-provided link, saving it as an image.

    Args:
        link (str): The URL to encode into the QR code.
        filename (str, optional): The filename to save the image. Defaults to "qr_code.png".
        box_size (int, optional): The size of each box in pixels. Defaults to 10.
        border (int, optional): The width of the border around the QR code in pixels. Defaults to 4.

    Returns:
        None
    """

    try:
        # Create a QR code object with user-provided data and error correction
        qr = qrcode.QRCode(version=1, box_size=box_size, border=border, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(link)
        qr.make(fit=True)

        # Create an image from the QR code data
        img = qr.make_image(fill_color="black", back_color="white")

        # Ensure uniqueness in filename before saving
        if os.path.exists(filename):
            i = 1
            base, ext = os.path.splitext(filename)
            while os.path.exists(f"{base}_{i}{ext}"):
                i += 1
            filename = f"{base}_{i}{ext}"

        # Save the QR code image
        img.save(filename)
        print(f"QR code successfully generated and saved as: {filename}")

    except Exception as e:
        print(f"An error occurred while creating the QR code: {e}")

if __name__ == "__main__":
    while True:
        link = input("Enter the link you want to encode into a QR code (or \"q\" to quit): ")
        if link.lower() == "q":
            break
        create_qr_code(link)
