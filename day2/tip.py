bill = float(input())
tip_percent = float(input())
tip = (tip_percent / 100) * bill
total = bill + tip
print(f"Tip amount: ${tip}")
print(f"Total to pay: ${total}")

