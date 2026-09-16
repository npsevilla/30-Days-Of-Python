import math

# Level 1 & 2 Tasks
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)
print(3 ** 4)
print(3 // 4)   

print("Brad")
print("Pitt")
print("Australia")
print("I am enjoying 30 days of python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Brad"))
print(type("Pitt"))

# Level 3 & Senior Dev Challenge
print(f"Integer: {10}")
print(f"Float: {9.8}")
print(f"Complex: {4-4j}")
print(f"String: {"Brad"}")
print(f"Boolean: {True}")
print(f"List: {['apple', 'banana', 'kiwi']}")
print(f"Tuple: {(1, 2, 3)}")
my_set = {1, 2, 3}
print(f"Set: {my_set}")
print(f"Dictionary: {{'a': 1, 'b': 2, 'c': 3}}")

point_A = {"x" : 2, "y" : 3}
point_B = {"x" : 10, "y" : 8}

x_2 = point_B["x"]
y_2 = point_B["y"]
x_1 = point_A["x"]
y_1 = point_A["y"]

euclidian_distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

print(f"The distance between point A and point B is: {euclidian_distance:.2f}")



