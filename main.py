def is_even(number):
    return number % 2 == 0

number_to_check = int(input("Введіть число для перевірки: "))

if is_even(number_to_check):
    print(f"{number_to_check} є парним числом.")
else:
    print(f"{number_to_check} є непарним числом.")