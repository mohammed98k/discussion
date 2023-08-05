def triangle():
    x = int(input("base length:"))
    y = int(input("height:"))
    a = int(input("length 2:"))
    b = int(input("length 3:"))
    area = (x * y) / 2
    perimeter = x + a + b
    print("area:", area, "perimeter:", perimeter)


triangle()


def square():
    z = int(input("length:"))
    area = (z * z)
    perimeter = z * 4
    print("area:", area, "perimeter:", perimeter)


square()


