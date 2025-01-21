import qrcode
import tkinter as tk
from tkinter import filedialog

# Function to generate a QR code
def generate_qr_code():
    data = data_entry.get()
    file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    
    if data and file_name:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)
        status_label.config(text=f"QR code saved as {file_name}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and configure GUI components
data_label = tk.Label(root, text="Enter the data to encode:")
data_label.pack()

data_entry = tk.Entry(root)
data_entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI main loop
root.mainloop()
