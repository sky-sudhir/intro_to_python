item1price=input("Enter price of item 1")
quantityitem1=input("Enter quantity of item 1")
item2price=input("Enter price of item 2")
quantityitem2=input("Enter quantity of item 2")
item3price=input("Enter price of item 3")
quantityitem3=input("Enter quantity of item 3")

item1=int(item1price)*int(quantityitem1)
item2=int(item2price)*int(quantityitem2)
item3=int(item3price)*int(quantityitem3)
subtotal=item1+item2+item3

print(f"item 1: {int(item1price)} x by {quantityitem1}= {item1}")
print(f"item 2: {int(item2price)} x by {quantityitem2}= {item2}")
print(f"item 3: {int(item3price)} x by {quantityitem3}= {item3}")
print(f"Subtotal: {subtotal}")
tax=(8.5*subtotal)/100
print(f"tax 8.5%: {tax}")
print(f"total: {tax+subtotal}")

