first_name = "Sarah"
last_name = "Alsubaie"

print(first_name + " " + last_name)

print(len(first_name) + len(last_name))


print(first_name[0] + "." + last_name[0] + ".")


# -----------------------------------------------
first = float(input("First: "))
second = float(input("Second: "))

print("Sum:       ", round(first + second, 2))
print("Difference:", round(first - second, 2))
print("Product:   ", round(first * second, 2))
print("Division:  ", round(first / second, 2))
#-----------------------------------------------
Price = 25
Quantity = 4
Tax_Rate = 0.15        # 15%

Subtotal = Price * Quantity
Tax = Subtotal * Tax_Rate
Total = Subtotal + Tax

print(f"Subtotal : {Subtotal:.2f} SAR")
print(f"Tax : {Tax:.2f} SAR")
print(f"Total : {Total:.2f} SAR")