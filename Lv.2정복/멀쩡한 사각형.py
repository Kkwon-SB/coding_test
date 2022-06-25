# import math

# def solution(w,h):
#     return w * h - (w + h -math.gcd(w, h))


def solution(w, h):
    for i in range(min(w, h), 0, -1):
        if w % i == 0 and h % i == 0:
            return w * h - (w + h - i)

