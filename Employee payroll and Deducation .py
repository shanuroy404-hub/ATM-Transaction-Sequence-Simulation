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

Here is the flowchart code for Salary Slip Computation. You can paste it into a Mermaid editor to generate the flowchart.

flowchart TD
    A([Start]) --> B[/Enter employee name, basic salary, overtime and incentives/]
    B --> C[Calculate DA = basic * 0.42]
    C --> D[Calculate HRA = basic * 0.20]
    D --> E[Calculate Gross Salary = basic + DA + HRA + overtime + incentives]
    E --> F[Calculate PF = basic * 0.12]
    F --> G[Calculate Tax = gross * 0.05]
    G --> H[Calculate Deductions = PF + Tax]
    H --> I[Calculate Net Salary = gross - deductions]
    I --> J[/Display Salary Slip: Name, Basic, DA, HRA, Overtime, Incentives, Gross Salary, Deductions and Net Salary/]
    J --> K([Stop])
To view the flowchart: Open [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com), paste the code into the editor, and the flowchart will appear automatically.
