list = [18, 31, 47, 54, 39, 104]

even_numbers = ""

for number in list:
    if number % 2 == 0:
        even_numbers += str(number) + ","

even_numbers = even_numbers[:-1]

print("This is the list: ", list)
print("These are the even numbers: " + even_numbers)
