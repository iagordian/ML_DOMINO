
import numpy as np

def simmetric_marc(data: np.array) -> int:

    data = data[::-1]
    max_step = data.shape[0] // 2
    step = 1

    exsit = 0

    while True:        

        target = data[:step]
        other = data[step:]
        end = other.shape[0] - step + 1

        for i in range(end):

            window = other[i: i + step]

            if any([
                np.sum(target == window) == step,
                np.sum(target == window[::-1]) == step
            ]):
                exsit = max(step + int(not i or i == end - 1), exsit)

        step += 1

        if step > max_step:
            break

    return exsit