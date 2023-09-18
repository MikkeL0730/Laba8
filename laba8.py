#выполняет проверку на ровно одну нечетную цифру на четной позиции и палиндромичность числа, выводит числа, удовлетворяющие обоим условиям
import tkinter as tk
from tkinter import scrolledtext
global result

def has_one_odd_digit_at_even_position(num): #одна ли нечётная цифры на чётных позициях
    num_str = str(num)
    count_odd = 0
    for i in range(1, len(num_str), 2):
        if int(num_str[i]) % 2 != 0:
            count_odd += 1
    return count_odd == 1

def is_palindrome(num): #является ли число палиндромом
    num_str = str(num)
    return num_str == num_str[::-1]

def print_numbers_with_one_odd_digit_and_palindrome(n):
    result = ""
    n = int(n)
    for num in range(1, n+1):
        if has_one_odd_digit_at_even_position(num) and is_palindrome(num):
            output_text.insert(tk.END, str(num) + "\n")
    return result

def button_click():
    output_text.delete("1.0", tk.END)
    input_text = input_field.get()
    if(input_text == ""):
        output.config(text="Вы оставили окно пустым")
    elif (float(input_field.get()) < 11):
        output.config(text="Так как число меньше 11, то нет чисел удовлетворяющих условию")
    else:
        print_numbers_with_one_odd_digit_and_palindrome(input_text)
        output.config(text="Числа, в которых одна нечетная цифра на четной позиции и число является палиндромом:")
        #output_text.insert(tk.END, "1")

window = tk.Tk()
window.title("Лабораторная работа")

label = tk.Label(window, text="Введите натуральное число n (> 10):")
label.pack()

# Создание поля ввода
input_field = tk.Entry(window)
input_field.pack()

# Создание кнопки
button = tk.Button(window, text="Проверить", command=button_click)
button.pack()

output = tk.Label(window, text="Числа:")
output.pack()

# Создание прокручиваемого поля
output_text = scrolledtext.ScrolledText(window)
output_text.pack()

window.mainloop()
