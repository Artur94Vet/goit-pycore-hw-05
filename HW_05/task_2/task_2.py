'''
import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"(?<=\s)(\d+\.\d+)(?=\s)"
    for match in re.finditer(pattern, text):
        yield float(match.group(1))
        
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

if __name__ == '__main__':
    text = ("Загальний дохід працівника складається з декількох частин: "
            " 1000.01 як основний дохід, доповнений додатковими надходженнями "
            " 27.45 і 324.00 доларів. ")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")
'''

from colorama import init, Fore, Style
import re
from typing import Generator, Callable

# Ініціалізація colorama (autoreset=True скидає колір після кожного print)
init(autoreset=True)

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Функція шукає всі дійсні числа у тексті, які відокремлені пробілами з обох боків,
    або знаходяться в кінці рядка, і повертає їх як генератор типу float.
    """
    # Регулярний вираз: шукаємо числа у форматі "число.число"
    # (?<=\s) - перед числом має бути пробіл
    # (\d+\.\d+) - число у форматі 1000.01, наприклад
    # (?=\s|$) - після числа має бути пробіл або кінець рядка
    pattern = r"(?<=\s)(\d+\.\d+)(?=\s|$)"
    for match in re.finditer(pattern, text):
        yield float(match.group(1))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Функція підсумовує всі числа, що повертаються генератором func для заданого тексту.
    """
    return sum(func(text))

def main():
    # Приклад тексту, де в кінці рядка число без пробілу
    default_text = (
        "Загальний дохід працівника складається з декількох частин: "
        " 1000.01 як основний дохід, доповнений додатковими надходженнями "
        " 27.45 і 324.00"
    )
    
    while True:
        choice = input(
            Fore.CYAN + "Привіт! Бажаєте використати стандартний текст для обчислення доходу?\n"
            "Введіть 'Y' для стандартного тексту або 'T' для введення власного тексту.\n"
            "Для виходу введіть 'exit': " + Style.RESET_ALL
        ).strip().lower()
        
        if choice == "exit":
            print(Fore.MAGENTA + "Допобачення!" + Style.RESET_ALL)
            break
        elif choice == "y":
            text = default_text
        elif choice == "t":
            text = input(
                Fore.CYAN + "Введіть свій текст (суми надходжень повинні бути у форматі 100.00 в інакшому випадку все інше ігнорується): " + Style.RESET_ALL
            ).strip()
            if text.lower() == "exit":
                print(Fore.MAGENTA + "Допобачення!" + Style.RESET_ALL)
                break
        else:
            print(Fore.RED + "Невірна команда. Спробуйте ще раз." + Style.RESET_ALL)
            continue

        total_income = sum_profit(text, generator_numbers)
        print(Fore.GREEN + f"Загальний дохід: {total_income:.2f}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "Дякую, що скористалися цією можливістю!" + Style.RESET_ALL)
        break

if __name__ == "__main__":
    main()
