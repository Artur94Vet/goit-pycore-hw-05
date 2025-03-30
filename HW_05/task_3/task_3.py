import sys
import os
import re
from datetime import datetime
from functools import wraps
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def log_decorator(level: str):
    """
    Декоратор, який логуватиме виклик функції, включаючи дату, час, рівень логування,
    ім'я функції, аргументи та результат.
    """
    def actual_log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            current_time_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"{Fore.BLUE}{current_time_string} {level} Calling function {func.__name__} with arguments {args}, {kwargs} with result {result}{Style.RESET_ALL}")
            return result
        return wrapper
    return actual_log_decorator

@log_decorator("DEBUG")
def parse_log_line(line: str) -> dict:
    """
    Парсить рядок логу і повертає словник з ключами:
    'date', 'time', 'level', 'message'.
    Приклад:
    "2024-01-22 08:30:01 INFO User logged in successfully."
    """
    parts = line.strip().split()
    if len(parts) < 4:
        return {}
    date = parts[0]
    time = parts[1]
    level = parts[2].upper()
    message = " ".join(parts[3:])
    return {"date": date, "time": time, "level": level, "message": message}

@log_decorator("DEBUG")
def load_logs(file_path: str) -> list:
    """
    Завантажує лог-файл, парсить кожен рядок через parse_log_line
    і повертає список словників.
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(Fore.RED + f"Помилка: файл '{file_path}' не знайдено." + Style.RESET_ALL)
        exit(1)
    except Exception as e:
        print(Fore.RED + f"Виникла помилка при читанні файлу: {e}" + Style.RESET_ALL)
        exit(1)
    return logs

@log_decorator("DEBUG")
def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує список логів і повертає лише записи з заданим рівнем (без врахування регістру).
    """
    level = level.upper()
    return list(filter(lambda log: log.get("level") == level, logs))

@log_decorator("DEBUG")
def count_logs_by_level(logs: list) -> dict:
    """
    Підраховує кількість лог-записів для кожного рівня та повертає словник.
    """
    counts = {}
    for log in logs:
        lvl = log.get("level", "UNKNOWN")
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts

@log_decorator("DEBUG")
def display_log_counts(counts: dict):
    """
    Форматує та виводить таблицю з кількістю лог-записів для кожного рівня.
    """
    header = f"{Fore.YELLOW}{'Рівень логування':<18} | {'Кількість':<10}{Style.RESET_ALL}"
    separator = "-" * 32
    print(header)
    print(separator)
    for level in sorted(counts.keys()):
        print(f"{Fore.CYAN}{level:<18}{Style.RESET_ALL} | {Fore.GREEN}{counts[level]:<10}{Style.RESET_ALL}")

@log_decorator("DEBUG")
def display_logs(logs: list, level: str):
    """
    Виводить деталі лог-записів заданого рівня.
    """
    print(f"\n{Fore.YELLOW}Деталі логів для рівня '{level.upper()}':{Style.RESET_ALL}")
    for log in logs:
        print(f"{Fore.CYAN}{log['date']} {log['time']}{Style.RESET_ALL} - {log['message']}")

def main():
    # Інтерактивний режим: запитуємо шлях до лог-файлу та бажаний режим виводу
    default_path = r"D:\Python_new_project\goit-pycore-hw-05\HW_05\task_3\logfile.log"
    file_path = input(
        Fore.CYAN + "Введіть шлях до лог-файлу (натисніть Enter для використання стандартного): " + Style.RESET_ALL
    ).strip()
    if not file_path:
        file_path = default_path

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    
    print(f"\n{Fore.MAGENTA}Статистика логів за рівнями:{Style.RESET_ALL}")
    display_log_counts(counts)
    
    level = input(
        Fore.CYAN + "\nВведіть рівень логування для детального виведення (наприклад, ERROR), або натисніть Enter для завершення: " + Style.RESET_ALL
    ).strip()
    
    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            display_logs(filtered_logs, level)
        else:
            print(Fore.RED + f"Записів з рівнем '{level.upper()}' не знайдено." + Style.RESET_ALL)
    
    print(Fore.MAGENTA + "\nДопобачення!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()

