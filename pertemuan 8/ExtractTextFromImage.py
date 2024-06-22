from PIL import Image, ImageTk, ImageEnhance
import tkinter as tk
from tkinter import filedialog
from pytesseract import pytesseract

# Define path to Tesseract executable
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set Tesseract path
pytesseract.tesseract_cmd = path_to_tesseract

def open_image():
    # Open file dialog to choose an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])

    # Check if a file is selected
    if file_path:
        # Open image with PIL
        img = Image.open(file_path)

        # Enhance image contrast for better OCR
        img = ImageEnhance.Contrast(img).enhance(2.0)

        # Update the image on the GUI
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo

        # Extract text from the image
        text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')  # --psm 6 is used for sparse text
        text_var.set(text)

# Create the main window
root = tk.Tk()
root.title("Image to Text Converter")

# Add a title label
title_label = tk.Label(root, text="Image to Text Converter", font=("Helvetica", 16, "bold"), pady=10)
title_label.pack()

# Add labels for name, class, and NIM
name_label = tk.Label(root, text="Muhammad Faiz", font=("Helvetica", 12))
name_label.pack()

class_label = tk.Label(root, text="TI22D", font=("Helvetica", 12))
class_label.pack()

nim_label = tk.Label(root, text="220511139", font=("Helvetica", 12))
nim_label.pack()

# Create a button to open an image with style
open_button = tk.Button(root, text="Open Image", command=open_image, font=("Helvetica", 12), bg='lightblue', padx=10, pady=5)
open_button.pack(pady=10)

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()

# Create a label to display the extracted text
text_var = tk.StringVar()
text_label = tk.Label(root, textvariable=text_var, wraplength=400, font=("Helvetica", 12))
text_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
