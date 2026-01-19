payroll_records = []

def calculate_salary():
    name = input("Enter employee name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    salary = hours * rate
    payroll_records.append({"name": name, "salary": salary})
    print("Salary calculated successfully")

def view_payroll():
    if not payroll_records:
        print("No payroll records found")
    else:
        for record in payroll_records:
            print(record["name"], "- Salary:", record["salary"])

def main():
    while True:
        print("1. Calculate Salary")
        print("2. View Payroll")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            calculate_salary()
        elif choice == "2":
            view_payroll()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
