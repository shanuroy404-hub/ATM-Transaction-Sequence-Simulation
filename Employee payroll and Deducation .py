name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
da = basic * 0.42
hra = basic * 0.20
overtime = float(input("Enter overtime amount: "))
incentives = float(input("Enter incentives: "))

gross = basic + da + hra + overtime + incentives
pf = basic * 0.12
tax = gross * 0.05
deductions = pf + tax
net_salary = gross - deductions

print("\n----- Salary Slip -----")
print("Employee Name:", name)
print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("Overtime:", overtime)
print("Incentives:", incentives)
print("Gross Salary:", gross)
print("Total Deductions:", deductions)
print("Net Salary:", net_salary)
