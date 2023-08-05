def triangle():
    x = int(input("base length:"))
    y = int(input("height:"))

    area = (x * y) / 2

    print("area:", area)


triangle()


def rectangle():
    z = int(input("length:"))
    a = int(input("width"))
    area = z * a

    print("area:", area)


rectangle()


def circle():
    r = int(input("radius"))
    area = 3.14 * (r^2)
    print("area", area)
circle()