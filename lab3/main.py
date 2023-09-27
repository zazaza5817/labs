from math import sqrt, isclose
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x0, y0 = map(int, input().split())
# Вычисление сторон треугольника
sides = [sqrt((x1 - x2)**2 + (y1 - y2)**2), sqrt((x1 - x3)**2 + (y1 - y3)**2), sqrt((x2 - x3)**2 + (y2 - y3)**2)]
sides.sort()


ma = sqrt((2*sides[1]**2 + 2*sides[2]**2 - sides[0]**2)/4)
p = sum(sides)


print("Сумма длин сторон треугольника: %g" % p)
print("Длина медианы, проведенной из минимального угла: %g" % ma)

pr1 = (x1 - x0)*(y2 - y1)-(x2 - x1)*(y1 - y0)
pr2 = (x2 - x0)*(y3 - y2)-(x3 - x2)*(y2 - y0)
pr3 = (x3 - x0)*(y1 - y3)-(x1 - x3)*(y3 - y0)
inTriangle = False
if not (isclose(pr1, 0) or isclose(pr2, 0) or isclose(pr3, 0)):
    if sign(pr1) == sign(pr2) == sign(pr2):
        print("in")
