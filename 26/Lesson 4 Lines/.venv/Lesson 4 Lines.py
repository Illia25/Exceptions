# #завдання 1
# string = input('Enter a string: ')
#
# letter_count = 0
#
# digit_count = 0
#
# for char in string:
#
#    if char.isalpha():
#
#        letter_count += 1
#
#    elif char.isdigit():
#
#        digit_count += 1
#
# print('Number of letters:', letter_count)
#
# print('Number of digits:', digit_count)

#завдання 2
# # Отримати введений рядок від користувача
# input_str = input("Введіть рядок: ")
#
# # Отримати символ для пошуку
# search_char = input("Введіть символ для пошуку: ")
#
# # Ініціалізувати лічильник кількості входжень
# count = 0
#
# # Пройтися по кожному символу у введеному рядку
# for char in input_str:
#     # Перевірка, чи поточний символ співпадає із шуканим
#     if char == search_char:
#         count += 1
#
# # Вивести результат
# print(f"Символ '{search_char}' зустрічається у рядку {count} разів.")

#завдання 3
# string = input("Enter a string: ")
#
# search_word = input("Enter the word to search for: ")
#
# replace_word = input("Enter the word to replace it with: ")
#
# words = string.split()
#
# modified_words = []
#
# for word in words:
#
#    if word == search_word:
#
#        modified_words.append(replace_word)
#
#    else:
#
#        modified_words.append(word)
#
# modified_string = " ".join(modified_words)
#
# print(modified_string)

#завдання 4
# # Заданий рядок
# my_string = "Hello World!"
#
# # Виведення третього символу
# print(my_string[2])
#
# # Виведення передостаннього символу
# print(my_string[-2])
#
# # Виведення перших п'яти символів
# print(my_string[:5])
#
# # Виведення рядка без двох останніх символів
# print(my_string[:-2])
#
# # Виведення символів з парними індексами
# print(my_string[::2])
#
# # Виведення символів з непарними індексами
# print(my_string[1::2])
#
# # Виведення усіх символів у зворотному порядку
# print(my_string[::-1])
#
# # Виведення символів через один у зворотному порядку
# print(my_string[-1::-2])
#
# # Виведення довжини рядка
# print(len(my_string))