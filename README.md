# Banking System Using Python OOP

## 📌 Project Overview

The **Banking System Using Python OOP** is a console-based Python application developed to demonstrate the basic operations of a banking system using Object-Oriented Programming (OOP) concepts.

The application allows users to create customer accounts, deposit money, withdraw money, check the available balance, and record account activities in a text file. It uses abstraction, inheritance, encapsulation, and file handling to organize the program and manage account information.

## 🎯 Objectives

- To understand and implement Object-Oriented Programming concepts in Python.
- To simulate basic banking operations.
- To demonstrate abstraction, inheritance, and encapsulation.
- To store account information and transaction records using file handling.
- To improve Python programming and problem-solving skills.

## ✨ Features

- Create customer accounts.
- Store customer name, account number, account type, and initial balance.
- Deposit money into an account.
- Withdraw money with an insufficient balance check.
- Display the available account balance.
- Record account creation and transaction details in a text file.
- Handle account deletion and program exit choices.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Concepts:** Object-Oriented Programming (OOP)
- **OOP Principles:** Abstraction, Inheritance, Encapsulation
- **File Handling:** Text file operations
- **Python Module:** `abc` (Abstract Base Class)

## 🧠 OOP Concepts Implemented

### 1. Abstraction
The `Bank` class is an abstract class that defines the abstract method `display()`. The `Savings` class implements this method.

### 2. Inheritance
The `Customer` class inherits from `Bank`, and the `Savings` class inherits from `Customer`. This demonstrates multilevel inheritance.

### 3. Encapsulation
The customer account type and balance are stored using protected (`_acc_type`) and private (`__balance`) attributes.

### 4. File Handling
The program uses `accounts.txt` to record account creation details, deposits, withdrawals, account deletion, and exit activity.

## ⚙️ How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or Command Prompt.
4. Run the Python program using:

   ```bash
   python banking_system.py
   ```

   Replace `banking_system.py` with the actual Python filename if it is different.

5. Enter the customer and transaction details when prompted.
6. View the recorded information in `accounts.txt`, created in the program's working directory.

## 💻 Source Code

**Python Source Code:** [View Source Code](https://github.com/Reeshurajesh/Banking-System-/blob/c58f1b576cc1b974fc7b47b623e107f0764dba20/Oops%20%5BBanking%20Sysytem%5D.py)

## 📸 Output Screenshots

### 1. Account Creation
[View Screenshot](PASTE_ACCOUNT_CREATION_SCREENSHOT_LINK_HERE)

### 2. Deposit Operation
[View Screenshot](PASTE_DEPOSIT_SCREENSHOT_LINK_HERE)

### 3. Withdrawal Operation
[View Screenshot](PASTE_WITHDRAWAL_SCREENSHOT_LINK_HERE)

### 4. Available Balance
[View Screenshot](PASTE_BALANCE_SCREENSHOT_LINK_HERE)

### 5. Account Deletion
[View Screenshot](PASTE_ACCOUNT_DELETION_SCREENSHOT_LINK_HERE)

### 6. Exit Operation
[View Screenshot](PASTE_EXIT_SCREENSHOT_LINK_HERE)

### 7. File Handling Output
[View Screenshot](PASTE_FILE_OUTPUT_SCREENSHOT_LINK_HERE)

## 🚀 Future Enhancements

- Add a menu-driven interface for banking operations.
- Implement input validation and transaction amount checks.
- Add unique account number validation.
- Store account information in a database such as MySQL.
- Improve account deletion by removing or updating the corresponding account record.

## 👩‍💻 Author

**Reeshma Devi R**

Python Programming | Data Analytics Learner

## 📝 Conclusion

This project provides practical experience in Python Object-Oriented Programming and file handling by simulating essential banking operations. It demonstrates how abstraction, inheritance, and encapsulation can be used to structure a simple banking application.
