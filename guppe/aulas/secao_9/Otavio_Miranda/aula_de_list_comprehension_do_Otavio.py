def Division(x, y):
    return x / y


def Multiplication(x, y):
    return x * y


def Exponentiation(x, y):
    return x ** y


numbers = [1, 2, 3, 4, 5]
new_numbers = [number for number in numbers]
division = [number / 2 for number in numbers]
multiplication = [number * 2 for number in numbers]
exponentiation = [number ** 2 for number in numbers]

# new_numbers = []
# for number in numbers:
#     new_numbers.append(numero)

# new_numbers[0] = 20
print(numbers)
print(new_numbers)
print(division)
print(multiplication)
print(exponentiation)

