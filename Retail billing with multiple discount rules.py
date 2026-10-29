#Algorithm
Step 1: Start.

Step 2: Input the number of products.

Step 3: Initialize subtotal, total tax, and total discount to zero.

Step 4: For each product, input product name, category, price per unit, and quantity.

Step 5: Calculate the item amount.
\[
\text{Item Amount}=\text{Price}\times\text{Quantity}
\]

Step 6: Apply the category-specific tax rate and calculate the tax amount.
\[
\text{Tax}=\frac{\text{Item Amount}\times\text{Tax Rate}}{100}
\]

Step 7: Add the item amount and tax to their respective totals.

Step 8: Repeat Steps 4–7 until all products are processed.

Step 9: Check whether the subtotal meets the discount threshold. If yes, calculate the applicable discount; otherwise, set the discount to zero.

Step 10: Apply the maximum concession limit. If the calculated discount exceeds the limit, use the maximum permitted discount.

Step 11: Calculate the final bill amount.
\[
\text{Final Bill}=\text{Subtotal}+\text{Total Tax}-\text{Discount}
\]

Step 12: Display the itemized invoice containing product details, quantities, item amounts, taxes, discount, and final bill.

Step 13: Stop.
#Flowchart
             +------------------+
             |      START       |
             +------------------+
                      |
                      v
          +------------------------+
          | Input number of        |
          | products               |
          +------------------------+
                      |
                      v
          +------------------------+
          | Initialize subtotal,   |
          | tax and discount = 0   |
          +------------------------+
                      |
                      v
          +------------------------+
          | Input product name,    |
          | category, price,       |
          | quantity and tax rate  |
          +------------------------+
                      |
                      v
          +------------------------+
          | Calculate item amount  |
          | = price × quantity     |
          +------------------------+
                      |
                      v
          +------------------------+
          | Calculate category-    |
          | specific tax           |
          +------------------------+
                      |
                      v
          +------------------------+
          | Update subtotal and    |
          | total tax              |
          +------------------------+
                      |
                      v
          +------------------------+
          | Are all products       |
          | processed?             |
          +------------------------+
                | No        | Yes
                |           |
                +----<      v
          Input next   +-------------------+
          product      | Is subtotal >=    |
                       | discount threshold?|
                       +-------------------+
                         | No       | Yes
                         |          |
                         v          v
                  +-----------+  +------------------+
                  | Discount  |  | Calculate        |
                  | = 0       |  | applicable       |
                  +-----------+  | discount         |
                         |       +------------------+
                         |                |
                         |                v
                         |       +------------------+
                         |       | Is discount      |
                         |       | above maximum    |
                         |       | concession limit?|
                         |       +------------------+
                         |          | Yes     | No
                         |          v         |
                         |   +-------------+  |
                         |   | Set discount|  |
                         |   | to maximum  |  |
                         |   | limit       |  |
                         |   +-------------+  |
                         |          |         |
                         +----------+---------+
                                    |
                                    v
                       +------------------------+
                       | Calculate final bill   |
                       | = subtotal + tax       |
                       | - discount             |
                       +------------------------+
                                    |
                                    v
                       +------------------------+
                       | Display itemized       |
                       | invoice and final bill |
                       +------------------------+
                                    |
                                    v
                            +---------------+
                            |     STOP      |
                            +---------------+
#code
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
