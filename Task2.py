#Создайте функцию генератор чисел Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
size = 6
fib = iter(fibonacci())

for _ in range(size):
 print(next(fib))