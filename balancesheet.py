class BalanceSheet:
    def __init__(self, assets, liabilities, equity):
        self.assets = assets
        self.liabilities = liabilities
        self.equity = equity

    def display_balance_sheet(self):
        print("Balance Sheet")
        print("--------------")
        print(f"Assets: {self.assets}")
        print(f"Liabilities: {self.liabilities}")
        print(f"Equity: {self.equity}")
        print("--------------")
        total = self.assets + self.liabilities + self.equity
        print(f"Total: {total}")


# Hypothetical values for assets, liabilities, and equity
assets = 1000000
liabilities = 500000
equity = 500000

# Create a balance sheet instance and display the balance sheet
balance_sheet = BalanceSheet(assets, liabilities, equity)
balance_sheet.display_balance_sheet()
