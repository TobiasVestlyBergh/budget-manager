# Personal Budget Manager

## Description
This is a simple budget manager made in Python. You can add income and expenses, see your transactions and check your remaining balance. The transactions are saved in a JSON file.

## Setup
You need Python installed. Open the budget-manager folder in VS Code and use the terminal.

## How to Run

**Add an expense:**
```powershell
python src/budget_manager/cli.py add T001 2026-11-24 expense food 18.50 EUR
```

**Add income:**
```powershell
python src/budget_manager/cli.py add T002 2026-11-24 income salary 1000 EUR
```

**See transactions:**
```powershell
python src/budget_manager/cli.py list
```

**Check balance:**
```powershell
python src/budget_manager/cli.py summary
```

## Testing
I tested the program with normal and invalid transactions.

- **Normal test:** Added 1000 EUR income and 18.50 EUR expense. The balance was correctly calculated as 981.50 EUR.
- **Negative amount:** Tried adding -50 EUR. The program rejected it.
- **Invalid category:** Tried using "shopping". The program rejected it.

I also checked that the invalid transactions were not saved. All three tests passed.

## Data
Transactions are saved in `data/transactions.json`. I also included a CSV file with sample transactions.

## Known Limitations
The program only accepts certain categories and EUR as the currency. It checks the date format but does not check if the date actually exists. The sample CSV file is not automatically imported.