import json
import os
from datetime import datetime

class BankManagement:
    def __init__(self):
        self.accounts = {}
        self.file_name = "bank.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.accounts = json.load(file)
        else:
            self.accounts = {}

    def save_data(self):
        with open(self.file_name, "w") as file:
            json.dump(self.accounts, file, indent=4)
            
    def menu(self):
        while True:
            print("\n" + "=" * 55)
            print("          WELCOME TO BANK MANAGEMENT")
            print("=" * 55)

            print("1. Add User")
            print("2. Display User Information")
            print("3. Display All Users")
            print("4. Deposit Amount")
            print("5. Withdraw Amount")
            print("6. Check Balance")
            print("7. Display Transaction History")
            print("8. Delete Account")
            print("9. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_user()

            elif choice == "2":
                self.display_user_information()

            elif choice == "3":
                self.display_all_users()

            elif choice == "4":
                self.deposit_money()

            elif choice == "5":
                self.withdraw_money()

            elif choice == "6":
                self.check_balance()

            elif choice == "7":
                self.display_transaction_history()

            elif choice == "8":
                self.delete_account()

            elif choice == "9":
                print("\nThank you for using Bank Management System!")
                break

            else:
                print("\nInvalid choice! Please enter 1 to 9.")

    def add_user(self):
        print("\n--- Add User Information ---")

        account_no = input("Enter account number: ")
        if account_no in self.accounts:
            print("\nAccount already exists!")
            return

        user_name = input("Enter user name: ")

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("\nAge must be a number!")
            return

        phone_number = input("Enter phone number: ")
        account_type = input("Enter account type (Saving/Current): ")

        try:
            initial_deposit = float(input("Enter initial deposit amount: "))
        except ValueError:
            print("\nInvalid amount!")
            return

        if initial_deposit < 0:
            print("\nInitial deposit cannot be negative!")
            return

        # Store user information
        self.accounts[account_no] = {
            "user_name": user_name,
            "age": age,
            "phone_number": phone_number,
            "account_type": account_type,
            "balance": initial_deposit,
            "transactions": []
        }

        # Add initial deposit transaction
        self.accounts[account_no]["transactions"].append({
            "type": "Initial Deposit",
            "amount": initial_deposit,
            "balance": initial_deposit,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_data()

        print("\nAccount created successfully!")

    def display_user_information(self):
        print("\n--- User Information ---")

        account_no = input("Enter account number: ")
        if account_no not in self.accounts:
            print("\nAccount not found!")
            return

        user = self.accounts[account_no]

        print("\n" + "=" * 45)

        print("Account Number :", account_no)
        print("User Name      :", user["user_name"])
        print("Age            :", user["age"])
        print("Phone Number   :", user["phone_number"])
        print("Account Type   :", user["account_type"])
        print("Balance        :", user["balance"])

        print("=" * 45)

    def display_all_users(self):
        print("\n--- All Users ---")

        if len(self.accounts) == 0:
            print("\nNo users available.")
            return

        for account_no, user in self.accounts.items():
            print("\n" + "=" * 45)

            print("Account Number :", account_no)
            print("User Name      :", user["user_name"])
            print("Age            :", user["age"])
            print("Phone Number   :", user["phone_number"])
            print("Account Type   :", user["account_type"])
            print("Balance        :", user["balance"])

        print("=" * 45)
        
    def deposit_money(self):
        print("\n--- Deposit Amount ---")

        account_no = input("Enter account number: ")
        if account_no not in self.accounts:
            print("\nAccount not found!")
            return

        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("\nInvalid amount!")
            return

        if amount <= 0:
            print("\nDeposit amount must be greater than 0!")
            return

        user = self.accounts[account_no]

        # Update balance
        user["balance"] += amount

        # Save transaction
        user["transactions"].append({
            "type": "Deposit",
            "amount": amount,
            "balance": user["balance"],
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        self.save_data()

        print("\nAmount deposited successfully!")
        print("Deposited Amount :", amount)
        print("Current Balance  :", user["balance"])

    def withdraw_money(self):
        print("\n--- Withdraw Amount ---")

        account_no = input("Enter account number: ")
        if account_no not in self.accounts:
            print("\nAccount not found!")
            return

        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("\nInvalid amount!")
            return

        if amount <= 0:
            print("\nWithdrawal amount must be greater than 0!")
            return

        user = self.accounts[account_no]

        # Check balance
        if amount > user["balance"]:
            print("\nInsufficient balance!")
            print("Available Balance :", user["balance"])
            return

        # Update balance
        user["balance"] -= amount

        # Save transaction
        user["transactions"].append({
            "type": "Withdrawal",
            "amount": amount,
            "balance": user["balance"],
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        self.save_data()

        print("\nAmount withdrawn successfully!")
        print("Withdrawn Amount :", amount)
        print("Current Balance  :", user["balance"])

    def check_balance(self):
        print("\n--- Check Balance ---")

        account_no = input("Enter account number: ")
        if account_no not in self.accounts:
            print("\nAccount not found!")
            return

        user = self.accounts[account_no]

        print("\nAccount Number :", account_no)
        print("Account Holder :", user["user_name"])
        print("Balance        :", user["balance"])

    def display_transaction_history(self):
        print("\n--- Transaction History ---")

        account_no = input("Enter account number: ")
        if account_no not in self.accounts:
            print("\nAccount not found!")
            return

        user = self.accounts[account_no]
        transactions = user["transactions"]

        if len(transactions) == 0:
            print("\nNo transactions available.")
            return

        print("\n" + "=" * 55)

        print("Account Number :", account_no)
        print("Account Holder :", user["user_name"])

        print("=" * 55)

        for transaction in transactions:
            print("\nTransaction Type :", transaction["type"])
            print("Amount           :", transaction["amount"])
            print("Balance          :", transaction["balance"])
            print("Date             :", transaction["date"])
            
            print("-" * 55)
            
    def delete_account(self):
        print("\n--- Delete Account ---")

        account_no = input("Enter account number: ")
        if account_no not in self.accounts:
            print("\nAccount not found!")
            return
        user = self.accounts[account_no]
        
        print("\nAccount Holder :", user["user_name"])
        print("Balance        :", user["balance"])

        confirmation = input("\nAre you sure you want to delete this account? (yes/no): ")
        
        if confirmation.lower() == "yes":
            del self.accounts[account_no]
            self.save_data()
            print("\nAccount deleted successfully!")
        else:
            print("\nAccount deletion cancelled.")

bank = BankManagement()
bank.menu()