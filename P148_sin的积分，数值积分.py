from math import sin, cos, pi

def integrate(f, a, b, division):
    d = (b - a)/division
    s = 0
    for i in range(division):
        s += f(a + i * d)
    return a * d

print(integrate(sin, 0, pi, 100))
print(integrate(sin, pi, 0, 100))
print(integrate(cos, 0, pi/2, 100))