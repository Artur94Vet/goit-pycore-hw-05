from colorama import init, Fore, Style
import re
import os

# Ініціалізація colorama (autoreset=True автоматично скидає колір після кожного print)
init(autoreset=True)

# Визначаємо шлях до файлу phone_list.txt, що знаходиться в тій же директорії, що і скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "phone_list.txt")

def load_contacts():
    """
    Завантажує контакти з файлу phone_list.txt.
    Підтримує рядки з форматом name:phone або name,phone.
    Якщо файл не існує, повертає порожній словник.
    """
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    if ":" in line:
                        name, phone = line.split(":", 1)
                    elif "," in line:
                        name, phone = line.split(",", 1)
                    else:
                        continue
                    contacts[name.strip()] = phone.strip()
    return contacts

def save_contacts(contacts):
    """
    Зберігає контакти до файлу phone_list.txt.
    Записує контакти у форматі name:phone.
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return Fore.RED + "Enter user name." + Style.RESET_ALL
        except ValueError as ve:
            return Fore.RED + str(ve) + Style.RESET_ALL
        except IndexError:
            return Fore.RED + "Enter the argument for the command." + Style.RESET_ALL
        except Exception as e:
            return Fore.RED + f"Unexpected error: {e}" + Style.RESET_ALL
    return inner

def parse_input(user_input):
    """
    Розбиває введений рядок на команду та аргументи.
    Повертає кортеж (command, args), де command – рядок команди (у нижньому регістрі),
    а args – список аргументів.
    """
    parts = user_input.split()
    if not parts:
        return "", []
    command = parts[0].strip().lower()
    args = parts[1:]
    return command, args

def validate_phone(phone: str):
    """
    Перевіряє, чи відповідає номер телефону формату українського мобільного номера:
    має починатися з +380 та містити 9 цифр після нього.
    """
    pattern = r"^\+380\d{9}$"
    if not re.fullmatch(pattern, phone):
        raise ValueError("Phone number must be in Ukrainian format: +380XXXXXXXXX.")

@input_error
def add_contact(args, contacts):
    """
    Додає контакт до словника contacts та зберігає зміни у файлі.
    args має містити ім'я та номер телефону.
    Якщо передано недостатньо аргументів, піднімається IndexError.
    """
    if len(args) < 2:
        raise IndexError
    name, phone = args[0], args[1]
    validate_phone(phone)
    contacts[name] = phone
    save_contacts(contacts)
    return Fore.GREEN + "Contact added." + Style.RESET_ALL

@input_error
def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту та зберігає зміни у файлі.
    args має містити ім'я контакту та новий номер.
    Якщо передано недостатньо аргументів, піднімається IndexError.
    """
    if len(args) < 2:
        raise IndexError
    name, new_phone = args[0], args[1]
    validate_phone(new_phone)
    if name in contacts:
        contacts[name] = new_phone
        save_contacts(contacts)
        return Fore.GREEN + "Contact updated." + Style.RESET_ALL
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    """
    Повертає номер телефону для заданого контакту.
    Якщо аргументів недостатньо, піднімається IndexError.
    """
    if len(args) < 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return Fore.GREEN + contacts[name] + Style.RESET_ALL
    else:
        raise KeyError

def show_all(contacts):
    """
    Повертає рядок з усіма контактами та їх номерами, або повідомлення,
    якщо контактів немає.
    """
    if not contacts:
        return Fore.RED + "No contacts found." + Style.RESET_ALL
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = load_contacts()
    print(Fore.CYAN + "Welcome to the assistant bot!" + Style.RESET_ALL)
    while True:
        user_input = input(Fore.CYAN + "Enter a command: " + Style.RESET_ALL)
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print(Fore.MAGENTA + "Good bye!" + Style.RESET_ALL)
            break
        elif command == "hello":
            print(Fore.CYAN + "How can I help you?" + Style.RESET_ALL)
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(Fore.RED + "Invalid command. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
