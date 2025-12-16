import csv
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure"}]


key = ["name", "username", "department"]

with open("by_department.csv", "w") as department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
