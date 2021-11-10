# f = open('readme.md', 'r')

# license = f.readlines()
#     print(line)
# f.close()

# n = 2
#  * *
# * * *
#  * *

# n = 3
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *

# n = 4
#    * * * *
#   * * * * *
#  * * * * * *
# * * * * * * *
#  * * * * * *
#   * * * * *
#    * * * *


# n = 4

# f = open('result.txt', 'w')

# for i in range(n, 2*n):
#     current_string = ''*(2*n-1-i) + '*' * i + '\n'
#     f.write(current_string)


# for i in range(2*n-2, n-1, -1):
#     current_string = ''*(2*n-1-i) + '*' * i + '\n'
#     f.write(current_string)



# f.close()

# import requests

# print(requests.get('https://google.com/').text)

# import time
# import requests


# d = {}


# def benchmark(iter=10):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('До функции')
#             start = time.time()
#             result = func()
#             func_name = func.__qualname__
#             d.update(
#                 {
#                     func_name: d.get(func_name, 0) + 1
#                 }
#             )
#             import pdb; pdb.set_trace()
#             finish = time.time()
#             print('После функции')
#             print(f'Время выполнения функции: {(finish-start)/iter}')
#             return result
#         return wrapper
#     return decorator


# @benchmark(iter=5)
# def hello(name='world'):
#     print(f'Hello, {name}!')
#     # requests.get('https://google.com/')
#     time.sleep(0.5)

# @benchmark(iter=5)
# def name():
#     print(12435467)

# hello('Yan')
# name()

# hello('Yan')
# name()

# print(d)

# def countdown(n):
#     print('start working')
#     while n>0:
#         yield n
#         n -= 1
#         yield n


# timer = countdown(10)
# for t in timer:
#     print(t)

# list = ['a','b','c','d','e','f','g']
# gen = (x for x in list)

# print(type(gen))

# for x in gen:
#     print(x)

def check_logs(path=None):
    f= open(path, 'r')
    for i, l in enumerate(f):
        if 'error' in l:
            yield i+1
    f.close()


logger =check_logs('new.txt')
for log in logger:
    print(log)