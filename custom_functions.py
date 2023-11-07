def say_my_name():
    print("Hey, Number 1")


def say_my_name(name):
    print("Hey, I am " + name)


print()


def calculate_volume_cylinder(radius, height):
    vol = 22 / 7 * radius ** 2 * height
    print(vol)


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)


add_numbers(10, 20)
add_numbers(10.55, 44.5, 33.22, 11, 25, 71)
