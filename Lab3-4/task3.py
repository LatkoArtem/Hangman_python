time_spent = int(input("Enter the number of minutes spent per month: "))
payment = 100
if 0 <= time_spent <= 50:
    print("Payment: %s grn" % payment)
elif 50 < time_spent <= 100:
    payment += 50
    print("Payment: %s grn" % payment)
elif 100 < time_spent:
    excess = time_spent - 100
    payment = 150 + excess * 2
    print("Payment: %s grn" % payment)
else:
    print("The number of minutes cannot be negative!")