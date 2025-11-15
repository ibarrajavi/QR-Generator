import qrcode
from colorama import Fore, Style
import os

def normalize_name(base_name: str, default_ext: str = ".png") -> tuple[str, str, str]:
    """
    Helper function:
        - Splits the base_name into the filename and extension.
        - If the base_name doesn't have an extension, use the default_ext of '.png'.
    Output:
        - A tuple containing: base_name, filename, and extension.
    """

    filename, extension = os.path.splitext(base_name)

    if not extension:
        extension = default_ext
        base_name = base_name + extension
    
    return base_name, filename, extension

def create_name(base_name: str) -> str:
    """
    Create a file name for the QR code.
    If it already exists, increment it by one.
    
    Example:
        - qr_code.png -> qr_code_1.png
    """

    while True:
        # If the file name is blank, try again.
        if not base_name:
            base_name = input(f"{Fore.RED}File name cannot be blank.{Style.RESET_ALL} \nPlease try again: ").strip()
            continue
        # If the first letter of the base_name is not a letter or number, try again.
        if not base_name[0].isalnum():
            base_name = input(f"{Fore.RED}File name must begin with letter or number.{Style.RESET_ALL} \nPlease try again: ").strip()
            continue
        break # Once a valid file name is entered, break the loop.

    base_name, filename, extension = normalize_name(base_name)
    new_filename = base_name

    # If the file already exists, increment by one. Else, return the unmodified base_name
    counter = 0
    while os.path.exists(f"qr_codes/{new_filename}"):
        counter += 1
        new_filename = f"{filename}_{counter}{extension}"
    return new_filename
    
# Prompt the user for the URL, delete any erroneous whitespace.
url = input("Enter a URL for QR generation: ").strip()

# Blank URL error handling with retries.
while True:
    if not url:
        url = input(f"{Fore.RED}URL cannot be blank.{Style.RESET_ALL} \nPlease try again: ").strip()
        continue
    break

# Prompt the user for the file name.
name = input("Enter a file name for the QR: ").strip()
qr_name = create_name(name)

# Create the directory path for the QR getting generated.
qr_directory = 'qr_codes'
qr_path = f"{qr_directory}/{qr_name}"

# If the qr_directory of 'qr_codes/' doesn't exist, then create it.
if not os.path.exists(qr_directory):
    os.mkdir(qr_directory)
    print(f"Directory {qr_directory}/ created.")

# QR settings
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(qr_path)
print( f"{Fore.GREEN}QR successfully saved: {qr_path} {Style.RESET_ALL}")
