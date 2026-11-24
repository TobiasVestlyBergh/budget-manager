def create_transaction(transaction_id, date, kind, category, amount, currency):
    return {
        "id": transaction_id,
        "date": date,
        "kind": kind,
        "category": category,
        "amount": amount,
        "currency": currency
    }