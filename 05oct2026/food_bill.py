price=int(input("food price:"))
quantity=int(input("quantity:"))
charge=int(input("charge:"))
total=(price*quantity)+charge
discount=int(input("discount:"))/100*total
total_bill=total-discount
print(total_bill)