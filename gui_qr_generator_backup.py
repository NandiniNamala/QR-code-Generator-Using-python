import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode
import re

# Functions 

def generate_qr():
    data = input_entry.get().strip()

    if data == "":
        messagebox.showerror("Error", "Please enter Text or URL.")
        return

    # Validate only when URL mode is selected
    if mode.get() == "URL":
        pattern = r"^https?://.+"

        if not re.match(pattern, data):
            messagebox.showerror(
                "Invalid URL",
                "Please enter a valid URL starting with http:// or https://"
            )
            return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )

    if file_path:

        img = qrcode.make(data)

        img.save(file_path)

        # QR Preview
        preview = img.resize((180, 180))

        photo = ImageTk.PhotoImage(preview)

        preview_label.config(image=photo)

        preview_label.image = photo

        messagebox.showinfo(
            "Success",
            "QR Code Generated Successfully!"
        )


def clear():
    input_entry.delete(0, tk.END)
    preview_label.config(image="")
    preview_label.image = None


def copy_text():
    data = input_entry.get()

    if data == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Text or URL first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(data)

    messagebox.showinfo(
        "Copied",
        "Copied Successfully!"
    )

# Main Window 

root = tk.Tk()

root.title("QR Code Generator using Python")

root.geometry("600x700")

root.configure(bg="#F5F5F5")

# Logo 

try:
    logo = Image.open("assets/logo.png")
    logo = logo.resize((90, 90))
    logo_photo = ImageTk.PhotoImage(logo)

    logo_label = tk.Label(
        root,
        image=logo_photo,
        bg="#F5F5F5"
    )

    logo_label.pack(pady=10)

except:
    pass

# Title 

title = tk.Label(
    root,
    text="QR Code Generator using Python",
    font=("Segoe UI", 22, "bold"),
    bg="#F5F5F5",
    fg="#0078D7"
)

title.pack(pady=10)

# Mode 
mode = tk.StringVar(value="URL")

mode_label = tk.Label(
    root,
    text="Choose Input Type",
    font=("Segoe UI", 13, "bold"),
    bg="#F5F5F5"
)

mode_label.pack()

frame = tk.Frame(root, bg="#F5F5F5")
frame.pack()

url_radio = tk.Radiobutton(
    frame,
    text="URL",
    variable=mode,
    value="URL",
    bg="#F5F5F5",
    font=("Segoe UI", 11)
)

url_radio.grid(row=0, column=0, padx=20)

text_radio = tk.Radiobutton(
    frame,
    text="Text",
    variable=mode,
    value="TEXT",
    bg="#F5F5F5",
    font=("Segoe UI", 11)
)

text_radio.grid(row=0, column=1, padx=20)

# Input 

label = tk.Label(
    root,
    text="Enter Text or URL",
    font=("Segoe UI", 14),
    bg="#F5F5F5"
)

label.pack(pady=10)

input_entry = tk.Entry(
    root,
    width=45,
    font=("Segoe UI", 12)
)

input_entry.pack()

# Buttons 

generate_button = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=22,
    height=2,
    cursor="hand2"
)

generate_button.pack(pady=15)

copy_button = tk.Button(
    root,
    text="Copy Text / URL",
    command=copy_text,
    bg="#27AE60",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=22,
    cursor="hand2"
)

copy_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear,
    bg="#E74C3C",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=22,
    cursor="hand2"
)

clear_button.pack(pady=5)

# Preview 

preview_title = tk.Label(
    root,
    text="QR Code Preview",
    font=("Segoe UI", 15, "bold"),
    bg="#F5F5F5"
)

preview_title.pack(pady=20)

preview_label = tk.Label(
    root,
    bg="#F5F5F5"
)

preview_label.pack()

# Footer

footer = tk.Label(
    root,
    text="Developed using Python, Tkinter & QRCode Library",
    font=("Segoe UI", 10),
    bg="#F5F5F5",
    fg="gray"
)

footer.pack(side="bottom", pady=15)

# Run
root.mainloop()