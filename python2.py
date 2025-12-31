logs = [
    ["B101", "Anu", "BORROW", "2025-03-10"],
    ["B101", "Anu", "BORROW", "2025-03-10"],
    ["B102", "Bala", "RETURN", "2025-03-10"],
    ["B101", "Anu", "RETURN", "2025-03-10"],
    ["B103", "Chitra", "BORROW", "2025-03-11"]
]

book_counts = {}
borrow_status = {}
daily_counts = {}

for log in logs:
    bid, name, action, date = log

    if bid not in book_counts:
        book_counts[bid] = {"name": name, "BORROW": 0, "RETURN": 0}

    if action == "BORROW":
        book_counts[bid]["BORROW"] += 1
        borrow_status[bid] = borrow_status.get(bid, 0) + 1
    elif action == "RETURN":
        book_counts[bid]["RETURN"] += 1
        borrow_status[bid] = max(borrow_status.get(bid, 0) - 1, 0)

    daily_counts[date] = daily_counts.get(date, 0) + 1

print("LIBRARY ACTIVITY REPORT\n")
for bid, data in book_counts.items():
    print(f"{bid} | {data['name']} | Borrowed: {data['BORROW']} | Returned: {data['RETURN']}")

print("\nBOOK NOT RETURNED REPORT")
for bid, count in borrow_status.items():
    if count > 0:
        print(f"{bid} has books not returned")

print("\nDAILY LIBRARY STATISTICS")
for date, count in daily_counts.items():
    print(f"{date}: {count} activities")
