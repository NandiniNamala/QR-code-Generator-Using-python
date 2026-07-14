import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode

def generate_qr():
    url = url_entry.get()

    if url == "":
        messagebox.showerror("Error", "Please enter a website URL.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )

    if file_path:
        img = qrcode.make(url)
        img.save(file_path)
        messagebox.showinfo("Success", "QR Code generated successfully!")

def clear():
    url_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Smart QR Code Generator")
root.geometry("400x250")
root.configure(bg="#F5F5F5")

title = tk.Label(
    root,
    text="Smart QR Code Generator",
    font=("Arial", 18, "bold"),
    bg="#F5F5F5",
    fg="blue"
)
title.pack(pady=10)

label = tk.Label(root, text="Enter Website URL", bg="#F5F5F5")
label.pack(pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.pack()

generate_button = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr
)
generate_button.pack(pady=10)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear
)
clear_button.pack()

root.mainloop()
