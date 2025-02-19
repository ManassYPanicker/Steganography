# **Steganography Tool**

This repository contains two Python-based tools for **encrypting** and **decrypting** secret messages within images using **steganography**. The tools are built with a user-friendly GUI using the `customtkinter` library.

---

## **Features**
1. **Encryption Tool**:
   - Embeds a secret message and password into an image.
   - Saves the encrypted image as `encrypted_image.png`.

2. **Decryption Tool**:
   - Extracts the hidden message from an encrypted image.
   - Validates the password before revealing the message.

3. **User-Friendly GUI**:
   - Built with `customtkinter` for a modern look.
   - Supports dark/light mode toggling.
   - Includes image preview, message input, and password input fields.

4. **Error Handling**:
   - Ensures an image is selected before encryption/decryption.
   - Validates the presence of a message and password.
   - Handles incorrect passwords and missing hidden messages.

---

## **Requirements**
To run the application, you need the following Python libraries:
- `customtkinter`
- `Pillow` (PIL)
- `opencv-python` (cv2)
- `numpy`

You can install the required libraries using the following command:

```bash
pip install customtkinter pillow opencv-python numpy
```

---

## **How to Use**

![image](https://github.com/user-attachments/assets/a5516e81-85f2-4495-aa74-7638f572e10f)


### **1. Encryption Tool**
1. **Run the Encryption Tool**:
   - Execute the `encrypt.py` script.
   - A GUI window titled **"Steganography Encryption Tool"** will open.

2. **Select an Image**:
   - Click the **"Select Image"** button to choose an image file (supported formats: `.png`, `.jpg`, `.jpeg`).

3. **Enter Secret Message**:
   - In the **"Enter Secret Message"** field, type the message you want to hide.

4. **Enter Password**:
   - In the **"Enter Password"** field, provide a password for additional security.

5. **Encrypt the Message**:
   - Click the **"Encrypt"** button to embed the message into the image.
   - The encrypted image will be saved as `encrypted_image.png`.

6. **Success**:
   - A success message will appear, confirming that the message has been encrypted.

---

### **2. Decryption Tool**
1. **Run the Decryption Tool**:
   - Execute the `decrypt.py` script.
   - A GUI window titled **"Steganography Decryption Tool"** will open.

2. **Select the Encrypted Image**:
   - Click the **"Select Image"** button to choose the encrypted image (`encrypted_image.png`).

3. **Enter Password**:
   - In the **"Enter Password"** field, provide the password used during encryption.

4. **Decrypt the Message**:
   - Click the **"Decrypt"** button to extract the hidden message.

5. **View the Secret Message**:
   - If the password is correct, the secret message will be displayed in a pop-up window.
   - If the password is incorrect, an error message will appear.

---

## **Steps to Encrypt and Decrypt**

### **Encryption**
1. Select an image.
2. Enter a secret message.
3. Provide a password.
4. Click **"Encrypt"**.
5. The encrypted image (`encrypted_image.png`) will be saved in the current directory.

### **Decryption**
1. Select the encrypted image (`encrypted_image.png`).
2. Enter the password used during encryption.
3. Click **"Decrypt"**.
4. The secret message will be displayed if the password is correct.

## **Code Structure**
- **`encrypt.py`**:
  - Contains the code for embedding a secret message into an image.
- **`decrypt.py`**:
  - Contains the code for extracting a hidden message from an image.
---

## **Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---

## **Author**
[Manass Y Panicker](https://github.com/ManassYPanicker/Steganography)
