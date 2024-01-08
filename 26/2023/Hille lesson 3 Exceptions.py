# #завдання 1
# def get_day_name(day_number):
#     days = {
#         1: "понеділок",
#         2: "вівторок",
#         3: "середа",
#         4: "четвер",
#         5: "п'ятниця",
#         6: "субота",
#         7: "неділя"
#     }
#
#     try:
#         day_number = int(day_number)
#         return days[day_number]
#     except (ValueError, KeyError):
#         raise ValueError("Некоректний номер дня тижня")
#
# # Зчитування введеного номера дня тижня від користувача
# user_input = input("Введіть номер дня тижня (1-7): ")
#
# # Виведення результату
# try:
#     result = get_day_name(user_input)
#     print(result)
# except ValueError as e:
#     print(f"Помилка: {e}")

#завдання 2
# def compare_and_display_numbers(number1, number2):
#     try:
#         number1 = float(number1)
#         number2 = float(number2)
#
#         if number1 == number2:
#             return "Числа рівні."
#         else:
#             return f"Числа не рівні. У порядку зростання: {min(number1, number2)}, {max(number1, number2)}"
#     except ValueError as e:
#         return f"Помилка: {e}"
#
# # Зчитування введених користувачем чисел
# user_input1 = input("Введіть перше число: ")
# user_input2 = input("Введіть друге число: ")
#
# # Виведення результату
# result = compare_and_display_numbers(user_input1, user_input2)
# print(result)

#завдання 3
# def perform_operation(number1, number2, operator):
#     try:
#         number1 = float(number1)
#         number2 = float(number2)
#
#         if operator == '+':
#             result = number1 + number2
#         elif operator == '-':
#             result = number1 - number2
#         elif operator == '*':
#             result = number1 * number2
#         elif operator == '/':
#             # Обробка ділення на нуль
#             if number2 == 0:
#                 raise ValueError("Ділення на нуль неможливе.")
#             result = number1 / number2
#         else:
#             raise ValueError("Введено невірну математичну дію.")
#
#         return f"Результат: {result}"
#     except ValueError as e:
#         return f"Помилка: {e}"
#
# # Зчитування введених користувачем чисел та математичної дії
# user_input1 = input("Введіть перше число: ")
# user_input2 = input("Введіть друге число: ")
# user_operator = input("Введіть математичну дію (+, -, *, /): ")
#
# # Виведення результату
# result = perform_operation(user_input1, user_input2, user_operator)
# print(result)