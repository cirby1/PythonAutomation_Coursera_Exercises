import csv
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure"}]


keys = ["name", "username", "department"]

with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
