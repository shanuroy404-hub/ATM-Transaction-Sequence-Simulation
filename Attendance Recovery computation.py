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
