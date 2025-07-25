fruits=["mango","kiwi","banana"]
search="mango"
for fruit in  fruits:
    if fruit==search:
        print(search,"found")
else:
    print(search, "not found")

fruits=["mango","kiwi","banana"]
search="grapes"
for fruit in  fruits:
    if fruit==search:
        print(search,"found")
        break
else:
    print(search, "not found")

numbers=[12,34,56,78,90]
for num in numbers:
    if num%2==1:
        print("odd number found")
        break
        print(num)
else:
    print("all are even number ")