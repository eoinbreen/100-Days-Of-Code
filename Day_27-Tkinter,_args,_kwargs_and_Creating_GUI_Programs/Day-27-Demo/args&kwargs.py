def add(*nums):  # Takes in any number of arguments as a touple
    total = 0
    for n in nums:
        total += n
    return total


print(add(1, 2, 3, 4))


def calculate(n, **kwargs):  # Takes in any number for key word arguments as a dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # Use the get command to not return an error if nothing there in dictionary
        self.model = kw.get("model")
        self.colour = kw.get("colour")


my_car = Car(colour="Silver", make= "Nissan", model="Micra")
print(f"I drive a {my_car.colour} {my_car.make} {my_car.model}")