def calculate_monthly_compound_interest(x, r, n):
    total_amount = 0
    monthly_balances = []

    for i in range(1, n + 1):
        total_amount = total_amount * (1 + r) + x
        monthly_balances.append(total_amount)

    return monthly_balances


x = 1000  # Monthly deposit amount
r = 0.1  # Monthly interest rate (e.g., 1% per month)
n = 12  # Number of months

balances = calculate_monthly_compound_interest(x, r, n)
for month, balance in enumerate(balances, start=1):
    print(f"Month {month}: {balance:,.2f} VND")
