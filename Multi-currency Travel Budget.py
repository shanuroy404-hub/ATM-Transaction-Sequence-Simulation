#Algorithm
step 1: Start.

Step 2: Enter the total travel budget in the base currency, such as Indian Rupees (INR).

Step 3: Enter the number of expense categories, such as food, transport, accommodation, and shopping.

Step 4: For each expense category, enter the category name, expense amount in foreign currency, exchange rate, and conversion fee percentage.

Step 5: Convert the expense into the base currency.

Converted Amount = Foreign Currency Amount × Exchange Rate

Step 6: Calculate the conversion fee.

Conversion Fee = Converted Amount × Fee Percentage / 100

Step 7: Calculate the total expense for each category.

Total Category Expense = Converted Amount + Conversion Fee

Step 8: Add each category expense to calculate the total travel expenditure.

Step 9: Compare the total travel expenditure with the budget.
- If the total expenditure is within the budget, display “Within Budget.”
- Otherwise, display “Budget Exceeded” and calculate the excess amount.
Step 10: Identify the expense category with the largest total expense.

Step 11: Display the converted expenses, conversion fees, total expenditure, budget status, remaining or excess amount, and largest expense category.

Step 12: Stop.

#Flowchart
                ┌───────────────┐
                │     START     │
                └───────┬───────┘
                        |
                        v
          /----------------------------\
         / Enter travel budget and      \
         \ number of expense categories /
          \----------------------------/
                        |
                        v
          ┌────────────────────────────┐
          │ Initialize total expense   │
          │ and largest expense        │
          └─────────────┬──────────────┘
                        |
                        v
          /----------------------------\
         / Enter category, foreign      \
         \ amount, exchange rate and    /
          \ conversion fee percentage  /
                        |
                        v
          ┌────────────────────────────┐
          │ Convert expense to base    │
          │ currency                   │
          └─────────────┬──────────────┘
                        |
                        v
          ┌────────────────────────────┐
          │ Calculate conversion fee   │
          └─────────────┬──────────────┘
                        |
                        v
          ┌────────────────────────────┐
          │ Calculate category expense │
          │ Converted amount + fee     │
          └─────────────┬──────────────┘
                        |
                        v
                 ◇ More categories? ◇
                    /          \
                  Yes           No
                   |             |
                   └── Repeat    v
                       input  ┌─────────────────────┐
                              │ Calculate total     │
                              │ travel expenditure  │
                              └──────────┬──────────┘
                                         |
                                         v
                              ◇ Total > Budget? ◇
                                 /          \
                               Yes           No
                                |             |
                                v             v
                     /----------------\  /----------------\
                    / Display Budget   \ / Display Within  \
                    \ Exceeded         / \ Budget          /
                     \----------------/   \----------------/
                                |             |
                                └──────┬──────┘
                                       |
                                       v
                         ┌────────────────────────┐
                         │ Identify largest       │
                         │ expense category       │
                         └────────────┬───────────┘
                                      |
                                      v
                         /------------------------\
                        / Display converted costs, \
                       / fees, total expenditure,   \
                       \ budget status and largest  /
                        \ expense category          /
                         \------------------------/
                                      |
                                      v
                               ┌───────────┐
                               │   STOP    │
                               └───────────┘

#code
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
