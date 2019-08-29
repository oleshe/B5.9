"""
Вам предлагается написать декоратор для подобной логики, который измерял бы скорость работы функций. Как-то так:

@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass

Пара наблюдений:
1. В данном случае внутри вложенной функции (где-то в декораторе) стоит выводить среднее время выполнения.
2. Можно либо зафиксировать число запусков, либо передавать как параметр.
"""

def time_this(num_runs=10):
    def decorator(func):
        def wrap():
            import time
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
        return wrap
    return decorator

@time_this(num_runs=1000)
def f():
    for j in range(1000000):
        pass

if __name__ == '__main__':
    f()
