# app.py

import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

class UntanglerAI:
    def __init__(self, root):
        self.root = root
        self.root.title("UntanglerAI")

        # Dropdown categories
        self.categories = ["Faces", Architecture", "Symbols", "Cities", "Clothing", "Hair", "Timelines", "Colonial Bias"]
        self.selected_category = tk.StringVar(value=self.categories[0])

        ttk.Label(root, text="Choose Category:").pack(pady=5)
        self.dropdown = ttk.Combobox(root, values=self.categories, textvariable=self.selected_category)
        self.dropdown.pack(pady=5)

        # Buttons for image input
        ttk.Button(root, text="Upload Sora Image", command=self.upload_sora_image).pack(pady=5)
        ttk.Button(root, text="Upload Dataset Image", command=self.upload_dataset_image).pack(pady=5)

        # Canvas to display images
        self.sora_label = ttk.Label(root, text="Sora Image will appear here")
        self.sora_label.pack(pady=5)

        self.dataset_label = ttk.Label(root, text="Dataset Image will appear here")
        self.dataset_label.pack(pady=5)

    def upload_sora_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path).resize((300, 300))
            img = ImageTk.PhotoImage(img)
            self.sora_label.config(image=img)
            self.sora_label.image = img

    def upload_dataset_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path).resize((300, 300))
            img = ImageTk.PhotoImage(img)
            self.dataset_label.config(image=img)
            self.dataset_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = UntanglerAI(root)
    root.mainloop()


