

def circle_size (r):
    size = 3.14 * r * r
    return round(size, 2)
print(circle_size(2))

def square_size (a):
    return a * a
print(square_size(5))

def rectangle (a,b):
    return a * b
print(rectangle(3,8))

def triangle (a,h):
    return a * h / 2
print(int(triangle(6,3)))

def trapezoid (a,b,h):
    return (a + b) * h / 2
print(int(trapezoid(6,8,4)))

def circle_in_square (a):
    return a * a / 4 * 3.14
print(circle_in_square(8))

def square_in_circle (a):
    return a * a / 2 * 3.14
print(square_in_circle(4))

def circle_round (r):
    return round(r * 2 * 3.14 , 2)
print(circle_round(5))

def cylinder (r,h):
    return rectangle(circle_round(r) , h) + circle_size(r) * 2
print(cylinder(2,6))

def cylinder_v (r,h):
    return circle_size(r) * h
print(cylinder_v(2,6))

def cone (r,h):
    return cylinder_v(r,h) / 3
print(cone(2,6))