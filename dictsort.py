

def sort_list(keyname, oldlist):
    newlist = sorted(oldlist, key=lambda k: k[keyname])
    return newlist

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
            "lastname": "Jcobson",
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

sorted_value = str(input("Type Sorted Value Name :"))

# sorted_list = []
# sorted_list = sort_list(sorted_value, dict_list)

print('{:30s} {:20s} {:20s}'.format("Name", "| " + "Position", "| " + "Seperation Date"))
print('{:30s} {:20s} {:20s}'.format("_" * 30, "| " + "_" * 18, "| " + "_" * 18))
for person in sort_list(sorted_value, dict_list):
    print('{:30s} {:20s} {:20s}'.format(person["firstname"] + " " + person["lastname"], "| " + person["position"], "| " + person["seperationdate"]))

