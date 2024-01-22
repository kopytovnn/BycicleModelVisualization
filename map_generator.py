from math import sin


def sin_map():
    answer = []

    for x in range(100):
        y = 50 * sin(x / 10) + 200
        answer.append((x, y))
    return answer


def sin_t(t):
    phi = 0.2 * 3.14 * t
    x = 10 * t
    y = 50 * sin(t) + 200
    return phi, (x, y)
