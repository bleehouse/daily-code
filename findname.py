
dict_list = [
        {
            "firstname": "John",
            "lastname":  "Johnson",
            "position": "Manager",
            "seperationdate": "2016-12-31"
        },
        {
            "firstname": "Tou",
            "lastname": "Xiong",
            "position": "Software Engineer",
            "seperationdate": "2016-10-15"
        },
        {
            "firstname": "Michaela",
            "lastname": "Michaelson",
            "position": "District Manager",
            "seperationdate": "2016-12-19"
        },
        {
            "firstname": "Jake",
            "lastname": "Jacobson",
            "position": "Programmer",
            "seperationdate": ""
        },
        {
            "firstname": "Jacqelyn",
            "lastname": "Jackson",
            "position": "DBA",
            "seperationdate": ""
        },
        {
            "firstname": "Sally",
            "lastname": "Weber",
            "position": "Web Developer",
            "seperationdate": "2016-12-18"
        }
    ]

find_str = str(input("Enter a search string :"))

print('{:30s} {:20s} {:20s}'.format("Name", "| " + "Position", "| " + "Seperation Date"))
print('{:30s} {:20s} {:20s}'.format("_" * 30, "| " + "_" * 18, "| " + "_" * 18))

for person in dict_list:
    fullname = person["firstname"] + " " + person["lastname"]
    if fullname.find(find_str) > -1:
        print('{:30s} {:20s} {:20s}'.format(person["firstname"] + " " + person["lastname"], "| " + person["position"], "| " + person["seperationdate"]))