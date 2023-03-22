cars = ["ford","volvo","bmw"]
print(cars)
x = cars[0]
print(x)
cars[0] = "toyota"
print(cars)
x = len(cars)
print(x)
for x in cars:
    print(x)
cars.append("honda")
print(cars)
cars.pop(1)
print(cars)
cars.remove("honda")
print(cars)       