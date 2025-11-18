# OOP Bank Account Project

## About the Project

This Python project simulates a banking system using Object-Oriented Programming. It allows creating bank accounts, depositing and withdrawing money, transferring funds, and handling errors such as insufficient balance. The project also includes specialized account types with interest rewards and fees.

## Key Features

- Create and manage multiple bank accounts.
- Check account balances.
- Deposit funds with optional interest rewards.
- Withdraw funds with automatic balance checks and fees.
- Transfer money between accounts.
- Handle insufficient funds gracefully using custom exceptions.
- Demonstrates inheritance and method overriding.

## Classes and What They Do

### Exceptions

- `BalanceException`: Raised when a transaction cannot be completed due to insufficient funds.

### BankAccount

Represents a standard bank account.

- `__init__(self, initial_account, account_name)`: Create a new account.
- `get_balance()`: Display the current balance.
- `deposit(amount)`: Deposit money into the account.
- `viable_transaction(amount)`: Check if a transaction can be completed.
- `withdraw(amount)`: Withdraw money if available.
- `transfer(amount, account)`: Transfer money to another account.

### InterestRewardsAcct

A bank account that applies a 5% bonus on deposits.

- `deposit(amount)`: Override deposit to include interest reward.

### SavingsAcct

A savings account with withdrawal fees.

- `__init__(balance, name)`: Initialize savings account with a fee.
- `withdraw(amount)`: Override withdraw to include fee deduction.

## Example Usage

```python
# Create standard bank accounts
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

# Check balances
Dave.get_balance()
Sara.get_balance()

# Deposit money
Sara.deposit(500)

# Withdraw money
Dave.withdraw(10000)  # Fails
Dave.withdraw(10)       # Success

# Transfer money
Dave.transfer(10000, Sara)  # Fails
Dave.transfer(100, Sara)     # Success

# Interest reward account
Jim = InterestRewardsAcct(1000, "Jim")
Jim.get_balance()
Jim.deposit(100)
Jim.transfer(100, Dave)

# Savings account with fees
Blaze = SavingsAcct(1000, "Blaze")
Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(10000, Sara)  # Fails
Blaze.transfer(1000, Sara)   # Success
```

## Tech Stack

- Python 3.x

## Skills Gained

- Object-Oriented Programming: classes, inheritance, method overriding.
- Custom exception handling.
- Implementing real-world financial logic.
- Designing reusable and extendable classes.
- Working with deposits, withdrawals, and transfers.

## Takeaways

This project demonstrates how OOP can be used to simulate a banking system, handle errors elegantly, and extend functionality using inheritance. It highlights the importance of method overriding for specialized behavior and shows how to build a small, realistic financial application from scratch.
