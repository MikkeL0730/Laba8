#выполняет проверку на ровно одну нечетную цифру на четной позиции и палиндромичность числа, выводит числа, удовлетворяющие обоим условиям
import tkinter as tk

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
    result = []
    for num in range(1, n+1):
        if has_one_odd_digit_at_even_position(num) and is_palindrome(num):
            result.append(num)
    return result

def button_click():
    if(entry.get() == ""):
        output.config(text="Вы оставили окно пустым")
    elif (int(entry.get()) < 11):
        output.config(text="Так как число меньше 11, то нет чисел удовлетворяющих условию")
    else:
        n = int(entry.get())
        result = print_numbers_with_one_odd_digit_and_palindrome(n)
        output.config(text=result)

window = tk.Tk()
window.title("Number Checker")

label = tk.Label(window, text="Введите число n (> 10):")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Проверить", command=button_click)
button.pack()

output = tk.Label(window, text="")
output.pack()

window.mainloop()
