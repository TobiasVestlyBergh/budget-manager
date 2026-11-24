import argparse

from models import create_transaction
from validation import validate_transaction
from services import add_transaction, calculate_summary
from storage import load_transactions, save_transactions

parser = argparse.ArgumentParser()
commands = parser.add_subparsers(dest="command", required=True)

add = commands.add_parser("add")
add.add_argument("id")
add.add_argument("date")
add.add_argument("kind")
add.add_argument("category")
add.add_argument("amount", type=float)
add.add_argument("currency")

commands.add_parser("list")
commands.add_parser("summary")

args = parser.parse_args()
path = "data/transactions.json"
transactions = load_transactions(path)

if args.command == "add":
    transaction = create_transaction(
        args.id, args.date, args.kind,
        args.category, args.amount, args.currency
    )

    try:
        validate_transaction(transaction)
        for existing in transactions:
            if existing["id"] == transaction["id"]:
                raise ValueError("Transaction ID already exists")
        add_transaction(transactions, transaction)
        save_transactions(transactions, path)
        print("Transaction added")
    except ValueError as error:
        print(error)

elif args.command == "list":
    for transaction in transactions:
        print(transaction)

elif args.command == "summary":
    print(calculate_summary(transactions))