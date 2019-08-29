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

    def __enter__(self):
        return self.__call__

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

    def __exit__(self, exp_type, exp_value, exp_tr):
        pass

if __name__ == '__main__':
    with Time_This(100) as time_this :
        @time_this
        def f_2star():
            for j in range(1000000):
                pass
