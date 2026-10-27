total = 0
n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total = total + amount

    print("Product:", name)
    print("Amount:", amount)

if total >= 5000:
    discount = total * 0.10
elif total >= 2000:
    discount = total * 0.05
else:
    discount = 0

subtotal = total - discount
tax = subtotal * 0.05
final_bill = subtotal + tax

print("\n----- Retail Bill -----")
print("Total Amount:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", final_bill)
