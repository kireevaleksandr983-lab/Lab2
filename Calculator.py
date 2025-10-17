
"""
Простой калькулятор на Python
"""

def ADD(x,y):  # Ошибка 1: Нарушение PEP8 в имени функции и пробелы
    return x+y

def subtract(a,b):  # Ошибка 2: Неправильные пробелы вокруг параметров
    result = a - b
    return result

def multiply(a, b):
    c = a * b  # Ошибка 3: Избыточная переменная
    return c

def divide(a, b):  # Ошибка 4: Нет проверки деления на ноль
    return a / b

def power(a, b):  # Ошибка 5: Непонятное имя переменной
    r = 1
    for i in range(b):
        r = r * a
    return r  # Ошибка 6: Непонятное имя переменной 'r'

def main():
    print("Калькулятор!")
    
    while True:
        choice = input("Выберите операцию (1-5): ")  # Ошибка 7: Нет обработки неверного ввода
        
        if choice == '1':
            num1 = input("Введите первое число: ")  # Ошибка 8: Нет преобразования в float
            num2 = input("Введите второе число: ")
            result = ADD(num1, num2)
            print(f"Результат: {result}")
            
        elif choice == '2':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = subtract(num1, num2)
            print(f"Результат: {result}")
            
        elif choice == '3':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = multiply(num1, num2)
            if result > 100:  # Ошибка 9: Магическое число без пояснения
                print("Результат очень большой!")
            print(f"Результат: {result}")
            
        elif choice == '4':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = divide(num1, num2)  # Ошибка 10: Потенциальное деление на ноль
            print(f"Результат: {result}")
            
        elif choice == '5':
            num1 = float(input("Введите число: "))
            num2 = float(input("Введите степень: "))
            result = power(num1, num2)
            print(f"Результат: {result}")
            
        elif choice == '6':
            break
            
        else:
            print("Неверный выбор")  # Ошибка 11: Слишком краткое сообщение об ошибке

if name == "__main__":
    main()
