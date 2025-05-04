# Import the necessary modules
from tabulate import tabulate
import sys
import os  # Import os module to check file existence

# Define a constant for the transaction file
TRANSACTION_FILE = "transaction_history.txt"

# Define a class named "ATM" to represent the ATM functionality.
class ATM:
    # Initialize the ATM with an initial balance, current balance, and an empty transaction history.
    def __init__(self):
        self.initial_balance = 100000
        self.balance = self.initial_balance
        self.transaction_history = []
        self.load_transactions()  # Load transactions when ATM is initialized

    def load_transactions(self):
        if os.path.exists(TRANSACTION_FILE):
            with open(TRANSACTION_FILE, "r") as f:
                lines = f.readlines()
                self.transaction_history = [line.strip() for line in lines]
            self.balance = self.initial_balance
            for transaction in self.transaction_history:
                if transaction.startswith("Deposited"):
                    amount = float(transaction.split('$')[1].split(' ')[0])
                    self.balance += amount
                elif transaction.startswith("Withdrawn"):
                    amount = float(transaction.split('$')[1].split(' ')[0])
                    self.balance -= amount
                elif transaction.startswith("Transferred"):
                    amount = float(transaction.split('$')[1].split(' ')[0])
                    self.balance -= amount
        else:
            self.transaction_history = []

    def save_transaction(self, transaction_detail):
        self.transaction_history.append(transaction_detail)
        with open(TRANSACTION_FILE, "a") as f:
            f.write(transaction_detail + "\n")

    # Define a method for depositing money into the ATM.
    def deposit(self, amount):
        self.balance += amount
        transaction_detail = f'Deposited ${amount}'
        self.save_transaction(transaction_detail)  # Save transaction to file
        return f'Deposited ${amount}. New balance: ${self.balance}'

    # Define a method for withdrawing money from the ATM.
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            transaction_detail = f'Withdrawn ${amount}'
            self.save_transaction(transaction_detail)  # Save transaction to file
            return f'Withdrawn ${amount}. New balance: ${self.balance}'
        else:
            return 'Insufficient funds'

    # Define a method for transferring money from the ATM to another recipient.
    def transfer(self, amount, recipient, transfer_type):
        if amount <= self.balance:
            self.balance -= amount
            transaction_detail = f'Transferred ${amount} to {recipient}'
            self.save_transaction(transaction_detail)  # Save transaction to file
            return f'Transferred ${amount} to {recipient}. New balance: ${self.balance}'
        else:
            return 'Insufficient funds'

    # Define a method to get the current balance.
    def get_balance(self):
        return f'Current balance: ${self.balance}'

    # Define a method to get the transaction history.
    def get_transaction_history(self):
        return self.transaction_history

    # Function to display ATM logo
def display_logo():
    welcome_logo ="""
                        +==============================================================+
                        |██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗|
                        |██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝|
                        |██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  |
                        |██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  |
                        |╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗|
                        | ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝|
                        +==============================================================+
"""
    print(welcome_logo)

# Define a function named "atm_interface" to handle the ATM user interface.
def atm_interface():
    atm = ATM()
    display_logo()  # Display the ATM logo
    print("Welcome to the ATM Machine Simulation")
    print("Use Default User_id=123456 & pin=654321")
    user_id = input("Enter User ID: ")
    pin = input("Enter PIN: ")

    if user_id == "123456" and pin == "654321":
        print("Login successful!\n")
        while True:
            print(" ATM Operations:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. About")
            print("7. Quit")

            choice = input("Enter your choice (1/2/3/4/5/6/7): ")

            if choice == "1":
                amount = float(input("Enter the deposit amount: $"))
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                result = atm.deposit(amount)
                print(f"{result}\npass_code: {pass_code_display}")
            elif choice == "2":
                amount = float(input("Enter the withdrawal amount: $"))
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                result = atm.withdraw(amount)
                print(f"{result}\npass_code: {pass_code_display}")   
            elif choice == "3":
                print("Choose Transfer Type:")
                print("1. Account Transfer")
                print("2. Phone Transfer")
                print("3. Card Transfer")
                transfer_type = int(input("Enter your choice (1/2/3): "))

                amount = float(input("Enter the transfer amount: $"))
                recipient = input("Enter the recipient's name: ")

                transfer_details = f"Recipient: {recipient}"

                if transfer_type == 1:
                    account_no = input("Enter recipient's account number: ")
                    ifsc_code = input("Enter recipient's account IFSC code: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    transfer_details = f"Recipient: {recipient}\nAccount: {account_no}\nIFSC: {ifsc_code}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                elif transfer_type == 2:
                    phone_number = input("Enter recipient's phone number: ")
                    upi_id = input("Enter UPI ID: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    transfer_details = f"Recipient: {recipient}\nPhone: {phone_number}\nUPI: {upi_id}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                elif transfer_type == 3:
                    card_number = input("Enter recipient's card number: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    transfer_details = f"Recipient: {recipient}\nCard: {card_number}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                else:
                    result = "Invalid transfer type selection."
                    transfer_details = "N/A"
                print(result)
            elif choice == "4":
                balance = atm.get_balance()
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                print(f"{balance}\npass_code: {pass_code_display}\nAvailable Balance: ${atm.balance:.2f}")
            elif choice == "5":
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                history = atm.get_transaction_history()
                
                if len(history) > 0:
                    table = []
                    available_balance = atm.initial_balance
                    for i, transaction in enumerate(history, start=1):
                        transaction_parts = transaction.split('$')
                        if len(transaction_parts) > 1:
                            transaction_amount = float(transaction_parts[-1].split()[0])
                            if "Deposited" in transaction:
                                available_balance += transaction_amount
                            elif "Withdrawn" in transaction or "Transferred" in transaction:
                                available_balance -= transaction_amount
                        table.append([i, transaction, f"${available_balance:.2f}"])
                    print(tabulate(table, headers=["#", "Transaction", "Available Balance"], tablefmt="grid"))
                else:
                    print("Transaction history is empty.")
            elif choice == "6":
                print("""
                      ++====================================================================================================++
                      ||  About the Developer:                                                                              || 
                      ||  This project was developed by Pankaj Garkoti, a passionate Python developer                       ||
                      ||  with a strong interest in Python Development, FrontEnd Development and Android App Development.   ||
                      ||                                                                                                    ||
                      ||  Contact Information:                                                                              ||
                      ||  Email: pankajgarkoti935@gmail.com                                                                 ||
                      ||  GitHub: https://github.com/PankajGarkoti128                                                       ||
                      ||  LinkedIn: https://www.linkedin.com/in/pankaj-g-731473240                                          ||
                      ||                                                                                                    ||
                      ||  Contributions:                                                                                    ||
                      ||  If you'd like to contribute to this project or have suggestions for improvement,                  ||
                      ||  please feel free to:                                                                              ||
                      ||                                                                                                    ||    
                      ||  -Fork the repository on GitHub                                                                    ||    
                      ||  -Submit issues or feature requests                                                                ||  
                      ||  -Collaborate on new features                                                                      ||
                      ||                                                                                                    ||
                      ||  License:                                                                                          ||
                      ||  This project is licensed under Apache "2.0" See LICENSE.txt for details.                          ||
                      ++====================================================================================================++
                        """)


            # Check if the user's choice is "7" (Quit).
            elif choice == "7":
                # Print a thank you message and break out of the loop to exit the program.
                print("QUITING!")
                print("""
                        +==================================================================================+
                        |████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗ |
                        |╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║ |
                        |   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║    ██║ |
                        |   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║    ╚═╝ |
                        |   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝    ██╗ |
                        |   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝     ╚═╝ |
                        +==================================================================================+
                    """)
                print("Thank you for using the ATM Machine Simulation!")
                print("Have a great day!")
                break
            # Check if the user's choice is not a valid option.
            else:
                print("Invalid choice. Please enter a valid option.")

        
    # Check if the provided User ID and PIN are invalid.
    else:
        print("Invalid User ID or PIN. Exiting...")
        sys.exit() 

# Check if the script is being run as the main program.
if __name__ == "__main__":
    # Call the "atm_interface" function to start the ATM application.
    atm_interface()