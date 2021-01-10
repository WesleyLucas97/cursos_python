numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [number for number in numbers if number > 5]
odd = [number for number in numbers if number % 2 != 0]
even = [number for number in numbers if number % 2 == 0]
another_if = [
    number 
    if number != 6 else 600 
    for number in numbers 
    if number % 2 == 0
]
another_if_2 = [
    number
    if number != 8 else 800
    for number in even
]

print(numbers)
print(new_numbers)
print(odd)
print(even)
print(another_if)
print(another_if_2)
