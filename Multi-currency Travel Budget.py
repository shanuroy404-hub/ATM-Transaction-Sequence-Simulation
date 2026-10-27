budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))

expenses = []

for i in range(n):
    amount = float(input("Enter expense in foreign currency: "))
    expenses.append(amount)

rate = float(input("Enter exchange rate (INR per unit): "))
fee_percent = float(input("Enter conversion fee percentage: "))

total_foreign = sum(expenses)
converted_amount = total_foreign * rate
fee = converted_amount * fee_percent / 100
total_inr = converted_amount + fee

print("\n----- Travel Budget -----")
print("Total Foreign Expenses:", total_foreign)
print("Converted Amount in INR:", converted_amount)
print("Conversion Fee:", fee)
print("Total Cost in INR:", total_inr)

if total_inr <= budget:
    print("Travel expenses are within budget.")
else:
    print("Travel expenses exceed the budget.")

if expenses:
    largest = max(expenses)
    print("Largest Expense:", largest)
