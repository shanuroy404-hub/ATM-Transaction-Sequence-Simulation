attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
required = float(input("Enter required attendance percentage: "))

if conducted == 0:
    print("No classes have been conducted yet.")
elif attended < 0 or attended > conducted:
    print("Invalid attendance details.")
else:
    percentage = attended / conducted * 100
    print("Current Attendance:", percentage, "%")

    if percentage >= required:
        print("Attendance requirement is satisfied.")
    else:
        extra = 0

        while (attended + extra) / (conducted + extra) * 100 < required:
            extra += 1

        print("Additional consecutive classes required:", extra)

## Algorithm: Attendance Recovery Computation

Step 1: Start.

Step 2: Enter the number of classes attended, total classes conducted, and required attendance percentage.

Step 3: Check whether the total classes conducted is zero. If yes, display “No classes have been conducted yet.”

Step 4: Otherwise, check whether the classes attended are less than zero or greater than the total classes conducted. If yes, display “Invalid attendance details.”

Step 5: If the details are valid, calculate the current attendance percentage using:

\\[ \text{Percentage}=\frac{\text{Attended}}{\text{Conducted}}\times100 \\]

Step 6: Display the current attendance percentage.

Step 7: Check whether the current attendance percentage is greater than or equal to the required percentage.

- If yes, display “Attendance requirement is satisfied.”
- If no, initialize `extra = 0`.

Step 8: Using a `while` loop, check whether the attendance percentage after attending extra consecutive classes is still below the required percentage. If it is, increment `extra` by 1 and repeat the check.

Step 9: Display the additional consecutive classes required.

Step 10: Stop.

## Flowchart: Attendance Recovery Computation

flowchart TD
    A([Start]) --> B[/Enter attended, conducted, required percentage/]
    B --> C{Conducted == 0?}
    C -- Yes --> D[/Display No classes conducted/]
    D --> Z([Stop])
    C -- No --> E{Attended < 0 or Attended > Conducted?}
    E -- Yes --> F[/Display Invalid attendance details/]
    F --> Z
    E -- No --> G[Calculate percentage = attended / conducted * 100]
    G --> H[/Display current attendance percentage/]
    H --> I{Percentage >= required?}
    I -- Yes --> J[/Display Attendance requirement satisfied/]
    J --> Z
    I -- No --> K[Set extra = 0]
    K --> L{(attended + extra) / (conducted + extra) * 100 < required?}
    L -- Yes --> M[extra = extra + 1]
    M --> L
    L -- No --> N[/Display additional consecutive classes required/]
    N --> Z


### Flowchart symbols

- Oval: Start and Stop
- Parallelogram: Input and Output
- Rectangle: Calculation or process
- Diamond: Decision
- Arrow: Flow direction'''
