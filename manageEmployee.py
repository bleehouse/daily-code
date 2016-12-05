
employees = [
                "John Smith",
                "Jakie Jackson",
                "Chris Jones",
                "Amanda Cullen",
                "Jeremy GoodWin"
            ]
candadite = input("Enter an employee name to remove:").strip()

if candadite in employees:
    idx = employees.index(candadite)
    employees = employees[:idx] + employees[idx+1:]
    print(employees)
else:
    print(candadite + " is not in employees")
