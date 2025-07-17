def add_two_numbers(a, b):
    return a + b


def greet(name):
    print("Hello ", name, "!", sep="")


def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


def sum_list(arr):
    out = 0
    for n in arr:
        out += n
    return out


def print_days():
    days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    for day in days:
        print(day)


def check_sign(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")


def repeat_word(word, n):
    for _ in range(n):
        print(word)
