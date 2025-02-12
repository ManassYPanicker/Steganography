import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import cv2
import numpy as np

# Initialize CustomTkinter
ctk.set_default_color_theme("blue")

# Create the main window
app = ctk.CTk()
app.title("Steganography Decryption Tool")
app.geometry("600x700")

selected_image_path = None
END_MARKER = "@@@"  # Unique marker to indicate the end of the message

# Toggle Dark/Light Mode
def toggle_mode():
    if mode_switch.get() == 1:
        ctk.set_appearance_mode("dark")
        mode_switch.configure(text="Dark Mode")
    else:
        ctk.set_appearance_mode("light")
        mode_switch.configure(text="Light Mode")

# Select Image
def select_image():
    global selected_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        selected_image_path = file_path
        load_image(file_path)

# Load Image Preview
def load_image(file_path):
    img = Image.open(file_path)
    img = img.resize((250, 250), Image.LANCZOS)
    ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(250, 250))
    image_label.configure(image=ctk_image, text="")
    image_label.image = ctk_image

# Decrypt Message
def decrypt_message():
    if not selected_image_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    img = cv2.imread(selected_image_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return

    user_password = password_entry.get()
    if not user_password:
        messagebox.showerror("Error", "Please enter the decryption password!")
        return

    c = {i: chr(i) for i in range(256)}
    n, m, z = 0, 0, 0
    decrypted_message = ""

    while True:
        char = c.get(img[n, m, z], "")
        if char == "":
            break
        decrypted_message += char
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

        if decrypted_message.endswith(END_MARKER):
            decrypted_message = decrypted_message.replace(END_MARKER, "")
            break

    if ":" in decrypted_message:
        saved_password, secret_message = decrypted_message.split(":", 1)

        if user_password == saved_password:
            messagebox.showinfo("Decrypted Message", f"Secret Message: {secret_message}")
        else:
            messagebox.showerror("Error", "Incorrect password! Decryption failed.")
    else:
        messagebox.showerror("Error", "No hidden message found!")

# UI Elements
title_label = ctk.CTkLabel(app, text="Steganography Decryption Tool", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Dark Mode Toggle
mode_switch = ctk.CTkSwitch(app, command=toggle_mode)
mode_switch.pack(pady=5)

# Image Preview
image_label = ctk.CTkLabel(app, text="No Image Selected", width=250, height=250, fg_color="gray")
image_label.pack()

# Select Image Button
select_button = ctk.CTkButton(app, text="Select Image", command=select_image)
select_button.pack(pady=10)

# Password Input
password_label = ctk.CTkLabel(app, text="Enter Password:")
password_label.pack(pady=5)
password_entry = ctk.CTkEntry(app, width=400, show="*")  # Hide password input
password_entry.pack(pady=5)

# Decrypt Button
decrypt_button = ctk.CTkButton(app, text="Decrypt", command=decrypt_message)
decrypt_button.pack(pady=10)

# Set Initial Theme
current_mode = ctk.get_appearance_mode()
if current_mode == "Dark":
    mode_switch.select()
    mode_switch.configure(text="Dark Mode")
else:
    mode_switch.deselect()
    mode_switch.configure(text="Light Mode")

app.mainloop()