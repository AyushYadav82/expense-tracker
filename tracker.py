from datetime import datetime

expenses = []
initial_balance = 0.0

def get_remaining_balance():
    spent = sum(e['amount'] for e in expenses)
    return initial_balance - spent

def add_expense(timestamp, category, amount, note):
    if amount > get_remaining_balance():
        return False   # not enough balance

    expense = {
        "time": timestamp,
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)
    return True

def get_expenses():
    return expenses

def get_total_expense():
    return sum(e['amount'] for e in expenses)

def set_initial_balance(amount):
    global initial_balance
    initial_balance = amount

def get_initial_balance():
    return initial_balance