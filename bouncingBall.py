# h: height of ball
# bounce: height after touch earth
# window: height of window see ball
def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    result = 1
    h = h*bounce
    while window < h:
        result +=2
        h = h * bounce
    return result

# OR

from math import log

def bouncingBall(h, bounce, window):
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    return 1 + 2*int(log(window/float(h), bounce))