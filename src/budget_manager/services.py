def add_transaction(transactions, transaction):
    transactions.append(transaction)
    return transactions


def calculate_summary(transactions):
    income = 0
    expenses = 0

    for transaction in transactions:
        if transaction["kind"] == "income":
            income += transaction["amount"]
        else:
            expenses += transaction["amount"]

    return {
        "income": income,
        "expenses": expenses,
        "balance": income - expenses
    }
