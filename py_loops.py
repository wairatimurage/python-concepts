# while, for, each
from time import sleep

start = input("Enter the starting point:")
stop = input("Enter the stopping point:")

# print(type(start))
if start.isnumeric() and stop.isnumeric():
    start = int(start)
    stop = int(stop)
    counter = start

    while counter <= stop:
        print(f"Counting {counter}")
        sleep(3)
        counter += 1
else:
    print(f"Number is invalid. Enter integers only")

