def fibonacci(number):
    first = 1
    second = 1
    current = second
    print(first)
    while current < number:
        print(current)
        current = first + second
        first = second
        second = current

# print(fibonacci(10))

print(fibonacci(1000))