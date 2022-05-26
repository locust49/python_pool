from time import sleep, time


def ft_progress(listy):
    total = len(listy)
    start = time()
    for iteration in listy:
        elapsed_iteration = time() - start
        percentage = 100 * (iteration + 1) // total
        eta = ((total * elapsed_iteration) / (iteration + 1))\
            - elapsed_iteration
        bar = '=' * (49 * percentage // 100) + '>'
        print('ETA: {:.2f}s [{:>2}%][{:50}] {}/{} | elapsed time {:.4f}'
              .format(eta, percentage, bar, iteration + 1,
                      total, elapsed_iteration), end='\r')
        yield iteration


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
