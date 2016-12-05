with open("employee.txt") as f:
    employees = f.read().splitlines()


# employees = [line.rstrip('\n') for line in open("employee.txt")]
candadite = input("Enter an employee name to remove:").strip()

if candadite in employees:
    idx = employees.index(candadite)
    employees = employees[:idx] + employees[idx+1:]
    print(employees)
else:
    print(candadite + " is not in employees")
    print(employees)