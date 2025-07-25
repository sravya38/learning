amount=20000.000
if amount>15000:
    discount=amount*0.6
elif amount>10000:
    discount=amount*0.3
elif amount>1000:
    discount=amount*0.2
else:
    discunt=0

final_amount=amount-discount
print(f"amount={amount:.2f}")
print(f"discount={discount:.2f}")
print(f"final price={final_amount:.2f}")