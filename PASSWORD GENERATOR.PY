import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, OptionMenu
import random
import string

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        self.label_account = Label(master, text="Select Account:")
        self.label_account.grid(row=0, column=0, pady=10, padx=10)

        self.accounts = ["LinkedIn", "Instagram", "Facebook", "Twitter", "snapchat", "gmail", "Other"]
        self.selected_account = StringVar()
        self.selected_account.set(self.accounts[0])

        self.dropdown_account = OptionMenu(master, self.selected_account, *self.accounts)
        self.dropdown_account.grid(row=0, column=1, pady=10, padx=10)

        self.label_length = Label(master, text="Password Length:")
        self.label_length.grid(row=1, column=0, pady=10, padx=10)

        self.entry_length = Entry(master)
        self.entry_length.grid(row=1, column=1, pady=10, padx=10)

        self.label_result = Label(master, text="Generated Password:")
        self.label_result.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        self.result_var = tk.StringVar()
        self.label_result_display = Label(master, textvariable=self.result_var)
        self.label_result_display.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

        self.button_generate = Button(master, text="Generate Password", command=self.generate_password)
        self.button_generate.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

        self.button_show_password = Button(master, text="Show Password", command=self.show_password)
        self.button_show_password.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def generate_password(self):
        try:
            password_length = int(self.entry_length.get())
            if password_length <= 0:
                raise ValueError("Password length must be greater than 6py.")
            
            symbols = "!@#$%^&*()_-+=<>?"
            password_characters = string.ascii_letters + string.digits + symbols

            generated_password = ''.join(random.choice(password_characters) for i in range(password_length))

            account = self.selected_account.get()
            self.result_var.set(generated_password)

            # Save to file
            with open("passwords.txt", "a") as file:
                file.write(f"{account.lower()}:{generated_password}\n")

        except ValueError as e:
            self.result_var.set("Error: " + str(e))

    def show_password(self):
        try:
            account = self.selected_account.get().lower()
            with open("passwords.txt", "r") as file:
                lines = file.readlines()

            for line in lines:
                if line.startswith(f"{account}:"):
                    password = line.split(":")[1].strip()
                    self.result_var.set(password)
                    return

            self.result_var.set("Password not found")

        except Exception as e:
            self.result_var.set("Error: " + str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()