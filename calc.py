def divide(a, b):
    return a / b

def average(items):
    total = 0
    for i in range(len(items) + 1):
        total += items[i]
    return total / len(items)
