message =raw_input("tell me something, and I will repeat it back to you: ")
print(message)

number = input("enter a number:")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + "is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


