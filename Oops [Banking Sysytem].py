from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def display(self):
        pass


class Customer(Bank):

    def __init__(self, name, acc_no, acc_type, balance):
        self.name = name
        self.acc_no = acc_no
        self._acc_type = acc_type
        self.__balance = balance

    def create_account(self):
        file = open("accounts.txt", "a")
        file.write("ACCOUNT CREATED\n")
        file.write("Customer Name : " + self.name + "\n")
        file.write("Account Number : " + str(self.acc_no) + "\n")
        file.write("Account Type : " + self._acc_type + "\n")
        file.write("Balance : " + str(self.__balance) + "\n")
        file.close()

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited :", amount)

        file = open("accounts.txt", "a")
        file.write("Deposit : " + str(amount) + "\n")
        file.close()

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn :", amount)

            file = open("accounts.txt", "a")
            file.write("Withdraw : " + str(amount) + "\n")
            file.close()
        else:
            print("Insufficient Balance")

    def acc_balance(self):
        return self.__balance


class Savings(Customer):

    def display(self):
        print("Available Balance :", self.acc_balance())

    def __del__(self):
        print("Thank You")


n = int(input("Enter Number of Accounts : "))

for i in range(n):

    name = input("Enter Your Name : ")
    acc_type = input("Enter Account Type : ")
    acc_no = int(input("Enter Account Number : "))
    balance = int(input("Enter Initial Balance : "))

    obj = Savings(name, acc_no, acc_type, balance)

    obj.create_account()

    amount = int(input("Enter Deposit Amount : "))
    obj.deposit(amount)

    amount = int(input("Enter Withdraw Amount : "))
    obj.withdraw(amount)

    obj.display()

    while True:

        choice = input("Enter Your Choice : ")

        if choice == "delete":

            file = open("accounts.txt", "a")
            file.write("Account Deleted\n")
            file.close()

            print("Account Deleted")
            del obj
            break

        elif choice == "Exit":

            file = open("accounts.txt", "a")
            file.write("Exit\n")
            file.close()

            print("Exit")
            del obj
            exit()

        else:
            print("Invalid Choice")
