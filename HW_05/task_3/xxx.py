from datetime import datetime
from functools import wraps
'''
Написати код, який буде для функції виводити інофрмацію про її роботу
'''

'''
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
'''

# print('2024-01-22 13:30:30 INFO User logged in')

'''
2024-01-22 13:30:30 INFO Calling function sum_numbers with arguments 1, 2 with result of 3
'''

def log_decorator(level: str):
    def actual_log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # print(func)
            # print(args, kwargs)
            result = func(*args, **kwargs)
            current_time_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"{current_time_string} {level} Calling function {func.__name__} with arguments {args}, {kwargs} with result {result}")
            return result
        return wrapper
    return actual_log_decorator


@log_decorator("DEBUG")
def sum_numbers(num_a: int, num_b: int) -> int:
    '''Function that returns sum of two numbers'''
    return num_a + num_b

# print(sum_numbers(1, 2))
# print(sum_numbers.__name__)
# print(sum_numbers.__doc__)

# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# print(dir(sum_numbers))
# print(sum_numbers.__name__)

my_list = ["hello", 1, [1, 2, 3]]
# print("hello", 1, [1, 2, 3])
# print(my_list[0], my_list[1], my_list[2])
# print(*my_list)

number_list = [2, 3]
print(sum_numbers(*number_list))

my_dict = {"num_a": 5, "num_b": 7}
sum_numbers(**my_dict)

def example(**args):
    print(args)

example(a=1, b="hello", c=2, d=[4, 5, 6])