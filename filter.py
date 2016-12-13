
input_str = str(input("Enter a list of numbers, seperated by spaces :"))

number_list = input_str.split(" ")

even_list = []

for member in number_list:
    if int(member) % 2 == 0:
        even_list.append(member)

print("The even numbers are " + ",".join(even_list))
