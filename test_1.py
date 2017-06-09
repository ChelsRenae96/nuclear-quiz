Y(0)=5
Y'(t)=-2t
def rk4(f, t0, y0, vy, vt, h, n):
    vt = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (t1 - t0) / float(n)
    t0=vt[0] = t
    y0=vy[0] = y
    n=range(t)
    for i in range(1, n + 1):
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(t + h, y + k3)
        vt[i] = x = t0 + i * h
        vy[i] = y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        return (vt, vy)
def f(t, y):
    return y=t**2+5
    vt, vy = rk4(f, 0, 5, 10)
    for t, y in list(zip(vt, vy))[::10]:
        print t, y, y - (t**2 +5)

