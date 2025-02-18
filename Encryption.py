import cv2
from customtkinter import *
from CTkMessagebox import CTkMessagebox

# Set theme and appearance mode
set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Encryption function
def encrypt():
    image = image_path_encrypt.get()
    message = message_entry.get()
    password = password_entry_encrypt.get()
    if not image or not message or not password:
        CTkMessagebox(title="Error", message="Please fill in all fields.", icon="cancel")
        return
    img = cv2.imread(image)
    if img is None:
        CTkMessagebox(title="Error", message="Unable to load image.", icon="cancel")
        return
    # Save the passcode to a file for later use during decryption
    with open("passcode.txt", "w") as f:
        f.write(password)
    msg = message + "###"  # Add marker
    m, n, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3
    output_path = "encryptedImage.png"
    cv2.imwrite(output_path, img)
    CTkMessagebox(title="Success", message=f"Encrypted image saved as {output_path}", icon="check")

# Browse image function for encryption
def browse_image_encrypt():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if filepath:
        image_path_encrypt.set(filepath)

# Main App for Encryption
root = CTk()
root.title("Steganography Tool - Encryption")
root.geometry("600x500")

# Variables
image_path_encrypt = StringVar()

# Title
CTkLabel(root, text="Steganography Tool - Encryption", font=("Arial", 20, "bold")).pack(pady=10)

# Encryption Section
frame_encrypt = CTkFrame(root)
frame_encrypt.pack(pady=10, fill="x")

# Select Image for Encryption
CTkLabel(frame_encrypt, text="Select Image:").grid(row=0, column=0, sticky="w", padx=5)
CTkEntry(frame_encrypt, textvariable=image_path_encrypt, width=300).grid(row=0, column=1, padx=5)
CTkButton(frame_encrypt, text="Browse", command=browse_image_encrypt).grid(row=0, column=2, padx=5)

# Message and Passcode for Encryption
CTkLabel(frame_encrypt, text="Message:").grid(row=1, column=0, sticky="w", padx=5)
message_entry = CTkEntry(frame_encrypt, width=300)
message_entry.grid(row=1, column=1, pady=5)
CTkLabel(frame_encrypt, text="Passcode:").grid(row=2, column=0, sticky="w", padx=5)
password_entry_encrypt = CTkEntry(frame_encrypt, show="*", width=300)
password_entry_encrypt.grid(row=2, column=1, pady=5)
CTkButton(frame_encrypt, text="Encrypt", command=encrypt).grid(row=3, column=1, pady=10)

# Run the app
root.mainloop()
