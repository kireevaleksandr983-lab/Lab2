
def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль!")
    return a / b

def main():
    """Основная функция с консольным интерфейсом"""
    print("Калькулятор")
    print("===========")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход")
    
    while True:
        try:
            choice = input("\nВыберите операцию (1-5): ")
            
            if choice == '5':
                print("Выход из калькулятора.")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Неверный выбор. Попробуйте снова.")
                continue
            
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            if choice == '1':
                result = add(num1, num2)
                print(f"Результат: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Результат: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Результат: {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Результат: {num1} / {num2} = {result}")
                
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
