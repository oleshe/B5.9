"""
Вам предлагается написать декоратор для подобной логики, который измерял бы скорость работы функций. Как-то так:

@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass

Пара наблюдений:
1. В данном случае внутри вложенной функции (где-то в декораторе) стоит выводить среднее время выполнения.
2. Можно либо зафиксировать число запусков, либо передавать как параметр.
3. Задание с одной звездочкой: написать декоратор в качестве объекта класса-секундомера.
   Задание с двумя звездочками: написать декоратор в качестве объекта класса-секундомера, который можно использовать как контекстный менеджер.
"""

class Time_This :
    def __init__(self, num_runs=10) :
        self.num_runs = num_runs
    def __call__(self, func):
        import time
        avg_time = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            func()
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.num_runs
        print("Выполнение заняло в среднем %.5f секунд за %s прогонов" % (avg_time, self.num_runs))
        return func

time_this = Time_This(1000)

@time_this
def f_1star():
    for j in range(1000000):
        pass

if __name__ == '__main__':
    f_1star()
