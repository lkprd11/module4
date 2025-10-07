# #ex1
# # TODO: Write a program that determines the grade based on a score
# score = 85
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"Score: {score}, Grade: {grade}")

# # Résultat attendu :
# # Score: 85, Grade: B


# # TODO: Create a simple calculator that performs different operations
# a = 10
# b = 5
# operation = "mul"  # change to add / sub / div

# if operation == "add":
#     result = a + b
# elif operation == "sub":
#     result = a - b
# elif operation == "mul":
#     result = a * b
# elif operation == "div":
#     if b != 0:
#         result = a / b
#     else:
#         result = "Error: division by zero"
# else:
#     result = "Invalid operation"

# print(f"Operation: {operation}, Result: {result}")

# # Résultat attendu (si operation = "mul") :
# # Operation: mul, Result: 50


# # TODO: Write a program that checks if a year is a leap year
# year = 2024
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     leap = True
# else:
#     leap = False

# print(f"Year: {year}, Leap year? {leap}")

# # Résultat attendu :
# # Year: 2024, Leap year? True


# # TODO: Implement a program that determines the price of a movie ticket
# age = 70
# day = "Wednesday"

# if age < 12:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 7  # réduction senior

# # réduction spéciale le mercredi
# if day == "Wednesday":
#     price -= 2

# print(f"Age: {age}, Day: {day}, Ticket price: ${price}")

# # Résultat attendu :
# # Age: 70, Day: Wednesday, Ticket price: $5

# cities = ["Paris", "New York", "Tokyo", "Cairo", "Sydney"]
# print(cities)
