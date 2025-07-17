def find_largest(arr):
    out = arr[0]
    for n in arr[1:]:
        if n > out:
            out = n
    return out


def check_letter(word, letter):
    return letter in word


def count_to_number(n):
    for i in range(1, n + 1):
        print(i)
