def validate_transaction(transaction):
    if transaction["amount"] <= 0:
        raise ValueError("Amount must be greater than 0")

    if transaction["kind"] not in ["income", "expense"]:
        raise ValueError("Invalid transaction kind")

    if transaction["category"] not in ["food", "transport", "housing", "salary", "other"]:
        raise ValueError("Invalid category")
   
    if transaction["currency"] != "EUR":
        raise ValueError("Invalid currency")
    
    date = transaction["date"]

    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        raise ValueError("Invalid date")

    if not date.replace("-", "").isdigit():
        raise ValueError("Invalid date")

    return transaction
