def high_and_low(numbers):
    # split string by space character
    numbers = numbers.split(" ")
    # convert string array to int, also making list from them
    numbers = list(map(int, numbers))
    return max(numbers), min(numbers)

print(high_and_low("1 2 10 4 5"))