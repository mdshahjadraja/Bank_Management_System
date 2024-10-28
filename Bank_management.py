import tkinter as tk
from tkinter import messagebox


class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Please enter a valid deposit amount."
        self.balance += amount
        return f"Deposited: {amount}. New Balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Please enter a valid withdrawal amount."
        if amount > self.balance:
            return "Insufficient balance!"
        self.balance -= amount
        return f"Withdrew: {amount}. New Balance: {self.balance}"

    def display_balance(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            return "Account already exists!"
        else:
            new_account = Account(account_number, account_holder)
            self.accounts[account_number] = new_account
            return "Account created successfully!"

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


class BankApp:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Bank Management System")
        self.root.geometry("500x400")

        # Title Label
        self.title_label = tk.Label(root, text="Bank Management System", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Menu Buttons
        self.create_account_btn = tk.Button(root, text="Create Account", width=20, command=self.create_account_ui)
        self.create_account_btn.pack(pady=5)

        self.deposit_btn = tk.Button(root, text="Deposit", width=20, command=self.deposit_ui)
        self.deposit_btn.pack(pady=5)

        self.withdraw_btn = tk.Button(root, text="Withdraw", width=20, command=self.withdraw_ui)
        self.withdraw_btn.pack(pady=5)

        self.check_balance_btn = tk.Button(root, text="Check Balance", width=20, command=self.check_balance_ui)
        self.check_balance_btn.pack(pady=5)

        self.exit_btn = tk.Button(root, text="Exit", width=20, command=root.quit)
        self.exit_btn.pack(pady=5)

    def create_account_ui(self):
        account_window = tk.Toplevel(self.root)
        account_window.title("Create Account")
        account_window.geometry("400x250")

        tk.Label(account_window, text="Account Number:").pack(pady=5)
        account_number_entry = tk.Entry(account_window)
        account_number_entry.pack(pady=5)

        tk.Label(account_window, text="Account Holder:").pack(pady=5)
        account_holder_entry = tk.Entry(account_window)
        account_holder_entry.pack(pady=5)

        def create():
            account_number = account_number_entry.get()
            account_holder = account_holder_entry.get()
            message = self.bank.create_account(account_number, account_holder)
            messagebox.showinfo("Create Account", message)
            account_window.destroy()

        tk.Button(account_window, text="Create", command=create).pack(pady=20)

    def deposit_ui(self):
        deposit_window = tk.Toplevel(self.root)
        deposit_window.title("Deposit")
        deposit_window.geometry("400x250")

        tk.Label(deposit_window, text="Account Number:").pack(pady=5)
        account_number_entry = tk.Entry(deposit_window)
        account_number_entry.pack(pady=5)

        tk.Label(deposit_window, text="Amount:").pack(pady=5)
        amount_entry = tk.Entry(deposit_window)
        amount_entry.pack(pady=5)

        def deposit():
            account_number = account_number_entry.get()
            amount = float(amount_entry.get())
            account = self.bank.get_account(account_number)
            if account:
                message = account.deposit(amount)
                messagebox.showinfo("Deposit", message)
            else:
                messagebox.showerror("Error", "Account not found!")
            deposit_window.destroy()

        tk.Button(deposit_window, text="Deposit", command=deposit).pack(pady=20)

    def withdraw_ui(self):
        withdraw_window = tk.Toplevel(self.root)
        withdraw_window.title("Withdraw")
        withdraw_window.geometry("400x250")

        tk.Label(withdraw_window, text="Account Number:").pack(pady=5)
        account_number_entry = tk.Entry(withdraw_window)
        account_number_entry.pack(pady=5)

        tk.Label(withdraw_window, text="Amount:").pack(pady=5)
        amount_entry = tk.Entry(withdraw_window)
        amount_entry.pack(pady=5)

        def withdraw():
            account_number = account_number_entry.get()
            amount = float(amount_entry.get())
            account = self.bank.get_account(account_number)
            if account:
                message = account.withdraw(amount)
                messagebox.showinfo("Withdraw", message)
            else:
                messagebox.showerror("Error", "Account not found!")
            withdraw_window.destroy()

        tk.Button(withdraw_window, text="Withdraw", command=withdraw).pack(pady=20)

    def check_balance_ui(self):
        balance_window = tk.Toplevel(self.root)
        balance_window.title("Check Balance")
        balance_window.geometry("400x200")

        tk.Label(balance_window, text="Account Number:").pack(pady=5)
        account_number_entry = tk.Entry(balance_window)
        account_number_entry.pack(pady=5)

        def check_balance():
            account_number = account_number_entry.get()
            account = self.bank.get_account(account_number)
            if account:
                message = account.display_balance()
                messagebox.showinfo("Balance", message)
            else:
                messagebox.showerror("Error", "Account not found!")
            balance_window.destroy()

        tk.Button(balance_window, text="Check Balance", command=check_balance).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
