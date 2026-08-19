# 🏦 Bank Management System

A simple command-line based Bank Management System built in Python that allows users to manage bank accounts with features like deposits, withdrawals, and transaction history — all persisted locally using a JSON file.

---

## 📋 Features

- **Add User** — Create a new bank account with personal details and an initial deposit
- **Display User Information** — View details of a specific account
- **Display All Users** — List all registered accounts
- **Deposit Amount** — Add funds to an existing account
- **Withdraw Amount** — Withdraw funds with balance validation
- **Check Balance** — Quickly view the current balance of an account
- **Transaction History** — View a full log of all transactions for an account
- **Delete Account** — Permanently remove an account with confirmation prompt
- **Data Persistence** — All data is automatically saved to and loaded from `bank.json`

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required (uses only built-in modules: `json`, `os`, `datetime`)

---

## 🚀 Getting Started

### 1. Clone or Download

```bash
git clone https://github.com/your-username/bank-management-system.git
cd bank-management-system
```

Or simply download `Bank_Management_System.py` directly.

### 2. Run the Application

```bash
python Bank_Management_System.py
```

---

## 🖥️ Usage

On launch, you will see the main menu:

```
=======================================================
          WELCOME TO BANK MANAGEMENT
=======================================================
1. Add User
2. Display User Information
3. Display All Users
4. Deposit Amount
5. Withdraw Amount
6. Check Balance
7. Display Transaction History
8. Delete Account
9. Exit
```

Enter the number corresponding to your desired action and follow the on-screen prompts.

### Example: Creating an Account

```
Enter account number: 1001
Enter user name: John Doe
Enter age: 30
Enter phone number: 9876543210
Enter account type (Saving/Current): Saving
Enter initial deposit amount: 5000

Account created successfully!
```

---

## 📁 Project Structure

```
bank-management-system/
│
├── Bank Management System.py   # Main application file
├── bank.json                   # Auto-generated data file (created on first run)
└── README.md                   # Project documentation
```

---

## 💾 Data Storage

All account data is stored in a `bank.json` file in the same directory. This file is created automatically on first use and updated after every transaction. Each account entry stores:

| Field          | Description                          |
|----------------|--------------------------------------|
| `user_name`    | Name of the account holder           |
| `age`          | Age of the account holder            |
| `phone_number` | Contact number                       |
| `account_type` | Saving or Current                    |
| `balance`      | Current account balance              |
| `transactions` | List of all transaction records      |

---

## ⚠️ Validations & Error Handling

- Duplicate account numbers are rejected
- Age and deposit/withdrawal amounts are validated as proper numbers
- Negative or zero amounts are not accepted for deposits or withdrawals
- Withdrawals exceeding the available balance are blocked
- Account deletion requires explicit `yes` confirmation

---

## 🔮 Possible Future Improvements

- Add PIN/password protection per account
- Implement fund transfer between accounts
- Add interest calculation for saving accounts
- Export transaction history to CSV or PDF
- Build a GUI using Tkinter or a web interface with Flask

---

## 📄 License

This project is open-source and free to use for educational purposes.
