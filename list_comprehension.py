def add(number):
    return number + number

n1 = [1,2,3,4,5]

result = map(add, n1)
print(list(result))