from tkinter import filedialog
from tkinter import Tk
from PIL import Image
import os

def encrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            encrypted_pixel = (pixel[2], pixel[1], pixel[0])
            img.putpixel((x, y), encrypted_pixel)
    
    encrypted_image_path = os.path.splitext(image_path)[0] + '_encrypted.png'
    img.save(encrypted_image_path)
    return encrypted_image_path

def decrypt_image(encrypted_image_path):
    img = Image.open(encrypted_image_path)
    width, height = img.size
    
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            decrypted_pixel = (pixel[2], pixel[1], pixel[0])
            img.putpixel((x, y), decrypted_pixel)
    
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    img.save(decrypted_image_path)
    return decrypted_image_path

def select_image():
    root = Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(title="Select Image File",
                                           filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")))
    root.destroy()
    
    if not file_path:
        print("No file selected. Exiting...")
        exit()
    
    return file_path

image_path = select_image()
encrypted_path = encrypt_image(image_path)
print(f"Image encrypted successfully! Encrypted image saved at: {encrypted_path}")

decrypted_path = decrypt_image(encrypted_path)
print(f"Image decrypted successfully! Decrypted image saved at: {decrypted_path}")
