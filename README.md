# Secure Data Hiding in Images Using Steganography

This project provides a Python-based steganography tool for securely hiding and extracting messages within images. It utilizes OpenCV and a graphical user interface (GUI) built with CustomTkinter to facilitate encryption and decryption.

## Features

- 🔒 Hide secret messages inside images securely
- 🕵️ Extract hidden messages from steganographic images
- 🔑 Password-protected encryption and decryption
- 🖼️ Supports common image formats (PNG, JPG, BMP)
- 🎨 User-friendly graphical interface

## Installation

To install and use the project, follow these steps:

```sh
# Clone the repository
git clone https://github.com/Bhavanach379/PyStego.git

# Navigate into the project directory
cd PyStego

# Install required dependencies
pip install -r requirements.txt
```

## Usage

### Encryption

To hide a message inside an image, run the encryption script:

```sh
python encrypt.py
```

1. 📁 Select an image file.
2. ✉️ Enter the secret message.
3. 🔢 Enter a passcode for encryption.
4. 🔏 Click "Encrypt" to generate the steganographic image.

The encrypted image will be saved as `encryptedImage.png`, and the passcode will be stored for decryption.

### Decryption

To extract a hidden message from an image, run the decryption script:

```sh
python decrypt.py
```

1. 📁 Select the encrypted image file.
2. 🔑 Enter the passcode used during encryption.
3. 🔓 Click "Decrypt" to reveal the hidden message.

If the passcode matches, the message will be displayed.

## Dependencies

Ensure you have the following dependencies installed:

- 🐍 Python 3.x
- 📸 OpenCV
- 🖌️ CustomTkinter

You can install them using:

```sh
pip install opencv-python customtkinter
```

## Screenshots

📷 Below are some screenshots demonstrating the encryption and decryption process:

*![Screenshot 2025-02-19 150844](https://github.com/user-attachments/assets/3a6e4f1e-ce3e-4aa7-be3e-a50ad15bc9d7)*
*![Screenshot 2025-02-16 144019](https://github.com/user-attachments/assets/48664674-4fc6-4ea9-8f2e-e0907ff7f6b8)*
*![Screenshot 2025-02-19 150925](https://github.com/user-attachments/assets/5da45ad5-a381-419f-8c0d-9cd6e63f5f23)*
*![Screenshot 2025-02-16 144139](https://github.com/user-attachments/assets/e025eac1-0e15-42cd-bbe1-2ae77e5c7487)*


## Contributing

🤝 Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.

## Contact

📧 For any questions or issues, contact Bhavana at bhavanach379@gmail.com.

