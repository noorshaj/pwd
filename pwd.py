import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("PASSWORD GENERATOR")
        self.root.geometry("400x300")
        
        # Variables
        self.password_length = tk.IntVar(value=00)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()
        
        # GUI Components
        tk.Label(root, text="Password Length:").pack(anchor="w", padx=10, pady=5)
        tk.Entry(root, textvariable=self.password_length).pack(anchor="w", padx=10, pady=5)
        
        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase).pack(anchor="w", padx=10, pady=5)
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.include_lowercase).pack(anchor="w", padx=10, pady=5)
        tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers).pack(anchor="w", padx=10, pady=5)
        tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special).pack(anchor="w", padx=10, pady=5)
        
        tk.Button(root, text="Generate Password", command=self.generate_password).pack(padx=10, pady=20)
        tk.Entry(root, textvariable=self.generated_password, state='readonly').pack(fill='x', padx=10, pady=5)
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(padx=10, pady=5)
    
    def generate_password(self):
        length = self.password_length.get()
        if length <= 0:
            messagebox.showerror("Invalid Length", "Password length must be greater than 0.")
            return
        
        character_pool = ''
        if self.include_uppercase.get():
            character_pool += string.ascii_uppercase
        if self.include_lowercase.get():
            character_pool += string.ascii_lowercase
        if self.include_numbers.get():
            character_pool += string.digits
        if self.include_special.get():
            character_pool += string.punctuation
        
        if not character_pool:
            messagebox.showerror("No Options Selected", "At least one character type must be selected.")
            return
        
        password = ''.join(random.choice(character_pool) for _ in range(length))
        self.generated_password.set(password)
        print(f"Generated Password: {password}")  # Debugging line
    
    def copy_to_clipboard(self):
        password = self.generated_password.get()
        print(f"Password to Copy: {password}")  # Debugging line
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied","Password copied to clipboard.")
            print("Password copied to clipboard.")  # Debugging line
        else:
            messagebox.showwarning("No Password", "Generate a password first.")
            print("No password to copy.")  # Debugging line

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
