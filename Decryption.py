import os
import cv2
from customtkinter import *
from CTkMessagebox import CTkMessagebox

# Set theme and appearance mode
set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Decryption function
def decrypt():
    encrypted_image_path = image_path_decrypt.get()
    password = password_entry_decrypt.get()
    # Read the original passcode from the file
    if not os.path.exists("passcode.txt"):
        CTkMessagebox(title="Error", message="Passcode file not found. Please encrypt first.", icon="cancel")
        return
    with open("passcode.txt", "r") as f:
        original_password = f.read().strip()
    if not encrypted_image_path or not password:
        CTkMessagebox(title="Error", message="Please fill in all fields.", icon="cancel")
        return
    if not os.path.exists(encrypted_image_path):
        CTkMessagebox(title="Error", message=f"Encrypted image '{encrypted_image_path}' not found.", icon="cancel")
        return
    img = cv2.imread(encrypted_image_path)
    if img is None:
        CTkMessagebox(title="Error", message="Unable to load encrypted image.", icon="cancel")
        return
    # Verify the passcode
    if password != original_password:
        CTkMessagebox(title="Error", message="YOU ARE NOT AUTHORIZED!", icon="cancel")
        return
    m, n, z = 0, 0, 0
    message = ""
    while True:
        char = chr(img[n, m, z])
        if char == "#":
            break
        message += char
        n += 1
        m += 1
        z = (z + 1) % 3
    CTkMessagebox(title="Decrypted Message", message=f"Decrypted message: {message}", icon="info")

# Browse image function for decryption
def browse_image_decrypt():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if filepath:
        image_path_decrypt.set(filepath)

# Main App for Decryption
root = CTk()
root.title("Steganography Tool - Decryption")
root.geometry("600x500")

# Variables
image_path_decrypt = StringVar()

# Title
CTkLabel(root, text="Steganography Tool - Decryption", font=("Arial", 20, "bold")).pack(pady=10)

# Decryption Section
frame_decrypt = CTkFrame(root)
frame_decrypt.pack(pady=10, fill="x")

# Select Image for Decryption
CTkLabel(frame_decrypt, text="Select Encrypted Image:").grid(row=0, column=0, sticky="w", padx=5)
CTkEntry(frame_decrypt, textvariable=image_path_decrypt, width=300).grid(row=0, column=1, padx=5)
CTkButton(frame_decrypt, text="Browse", command=browse_image_decrypt).grid(row=0, column=2, padx=5)

# Passcode for Decryption
CTkLabel(frame_decrypt, text="Passcode:").grid(row=1, column=0, sticky="w", padx=5)
password_entry_decrypt = CTkEntry(frame_decrypt, show="*", width=300)
password_entry_decrypt.grid(row=1, column=1, pady=5)
CTkButton(frame_decrypt, text="Decrypt", command=decrypt).grid(row=2, column=1, pady=10)

# Run the app
root.mainloop()
