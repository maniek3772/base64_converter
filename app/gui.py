import tkinter as tk
from tkinter import messagebox, scrolledtext
from app import encoder, decoder, utils


class Base64App:
    def __init__(self, root):
        self.root = root
        self.root.title("Base64 converter")

        # Input text
        self.input_text = scrolledtext.ScrolledText(root, width=60, height=10)
        self.input_text.pack(padx=10, pady=5)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Encode text", command=self.encode).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Decode text", command=self.decode).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Copy result", command=self.copy_result).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear).grid(row=0, column=3, padx=5)

        # Output
        self.output_text = scrolledtext.ScrolledText(root, width=60, height=10)
        self.output_text.pack(padx=10, pady=5)

    def encode(self):
        input_data = self.input_text.get("1.0", tk.END).strip()
        if not input_data:
            messagebox.showwarning("Warning", "Input field is empty.")
            return
        result = encoder.encode_text(input_data)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

    def decode(self):
        input_data = self.input_text.get("1.0", tk.END).strip()
        if not input_data:
            messagebox.showwarning("Warning", "Input field is empty.")
            return
        try:
            result = decoder.decode_text(input_data)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Base64 string.\n{e}")

    def copy_result(self):
        result_data = self.output_text.get("1.0", tk.END).strip()
        if result_data:
            utils.copy_to_clipboard(result_data)
            messagebox.showinfo("Success", "Result copied to clipboard.")

    def clear(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
