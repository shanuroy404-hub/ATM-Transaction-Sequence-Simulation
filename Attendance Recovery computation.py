#Algorithm
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

#Flowchart
              +----------------------+
              |        START         |
              +----------------------+
                         |
                         v
          +----------------------------+
          | Input total classes,       |
          | attended classes and       |
          | eligibility threshold      |
          +----------------------------+
                         |
                         v
          +----------------------------+
          | Validate input values      |
          +----------------------------+
                         |
                         v
                +----------------+
                | Input valid?   |
                +----------------+
                   | Yes    | No
                   v        v
          +----------------+  +------------------+
          | Calculate      |  | Display invalid  |
          | current        |  | input message    |
          | attendance %   |  +------------------+
          +----------------+          |
                   |                  v
                   v                +------+
          +------------------+      | STOP |
          | Attendance meets |      +------+
          | eligibility      |
          | threshold?       |
          +------------------+
              | Yes     | No
              v         v
      +---------------+ +----------------------+
      | Display       | | Initialize required  |
      | Eligible      | | consecutive classes  |
      +---------------+ | = 0                  |
              |         +----------------------+
              |                    |
              |                    v
              |         +----------------------+
              |         | Assume attendance at |
              |         | next class           |
              |         +----------------------+
              |                    |
              |                    v
              |         +----------------------+
              |         | Increase attended    |
              |         | and total classes    |
              |         | by 1; update count   |
              |         +----------------------+
              |                    |
              |                    v
              |         +----------------------+
              |         | Recalculate projected|
              |         | attendance %         |
              |         +----------------------+
              |                    |
              |                    v
              |         +----------------------+
              |         | Threshold reached?   |
              |         +----------------------+
              |            | No       | Yes
              |            |          |
              |            +----<     v
              |          Next class +------------------+
              |                     | Display minimum  |
              |                     | classes required |
              |                     +------------------+
              |                              |
              +------------------------------+
                                             |
                                             v
                                +------------------------+
                                | Evaluate other future  |
                                | attendance scenarios   |
                                +------------------------+
                                             |
                                             v
                                +------------------------+
                                | Display attendance and |
                                | scenario-wise results  |
                                +------------------------+
                                             |
                                             v
                                      +-----------+
                                      |   STOP    |
                                      +-----------+

#code
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

        print("Additional consecutive classes required:", extra")





