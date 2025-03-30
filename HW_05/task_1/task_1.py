'''def caching_fibonacci():
    """
    Функція caching_fibonacci створює внутрішню функцію fibonacci(n),
    яка обчислює n-те число Фібоначчі з використанням кешування результатів.
    """
    cache = {}  # Словник для збереження обчислених значень

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:  # Якщо результат для n вже обчислено, повертаємо його з кешу
            return cache[n]
        # Обчислюємо значення рекурсивно, зберігаємо в кеш та повертаємо результат
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання
if __name__ == '__main__':
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
'''
#  p.s. використовую всі можливі ресурси
from colorama import init, Fore, Style

# Ініціалізація colorama (autoreset=True автоматично скидає колір після кожного print)
init(autoreset=True)

def caching_fibonacci():
    """
    Створює замикання з кешем для обчислення чисел Фібоначчі.
    Повертає функцію fibonacci(n), яка використовує кеш для оптимізації.
    """
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

def main():
    fib = caching_fibonacci()
    
    while True:
        user_choice = input(
            Fore.CYAN + "Привіт, ти хочеш вивести результат домашнього завдання? " +
            "Введи 'Y' для демонстрації (результат дз), або 'число' для введення власного числа.\n" +
            "Або введи число безпосередньо.\n" +
            "Для виходу введи 'exit': " + Style.RESET_ALL
        ).strip().lower()
        
        if user_choice == "exit":
            print(Fore.MAGENTA + "Допобачення!" + Style.RESET_ALL)
            break

        # Якщо користувач обрав демонстрацію
        if user_choice == "y":
            result = fib(10)
            result_2 = fib(15)
            print(Fore.GREEN + f"Результат домашнього завдання (fib(10)): {result}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Результат домашнього завдання (fib(15)): {result_2}" + Style.RESET_ALL)
            print(Fore.MAGENTA + "Допобачення!" + Style.RESET_ALL)
            break

        # Якщо користувач вибрав варіант "число", спочатку запросимо число
        if user_choice == "число":
            num_input = input(Fore.CYAN + "Введіть ціле число: " + Style.RESET_ALL).strip()
        # Якщо користувач ввів число безпосередньо
        elif user_choice.lstrip("-").isdigit():
            num_input = user_choice
        else:
            print(Fore.RED + "Невірна команда. Будь ласка, спробуйте ще раз або введіть 'exit' для виходу." + Style.RESET_ALL)
            continue
        
        if num_input.lower() == "exit":
            print(Fore.MAGENTA + "Допобачення!" + Style.RESET_ALL)
            break
        
        try:
            n = int(num_input)
        except ValueError:
            print(Fore.RED + "Помилка: введене значення має бути цілим числом." + Style.RESET_ALL)
            continue

        result = fib(n)
        print(Fore.GREEN + f"Результат для введеного числа (fib({n})): {result}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "Дякую, що використали цю можливість" + Style.RESET_ALL)
        break

if __name__ == "__main__":
    main()
