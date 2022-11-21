print('I LOVE MOUNIKA')
print('OM NAMAH SHIVAYA')
print('MY FIRST PYTHON CODE IN PYCHARM EDITOR')
print("Testing GIT HUB0")
print("Testing GIT HUB1")
print("Testing GIT HUB2")
print("Testing GIT HUB3")
print("Testing GIT HUB4")
print("Testing GIT HUB5")
print("Testing GIT HUB6")
print("Testing GIT HUB7")
print("Testing GIT HUB8")
print("Testing GIT HUB Branches 1")
print("Testing GIT HUB Branches 2")

a = 2
print(a)

a, b, c = 7.8, 2, 'TEST'
print(a, b, c)

print("END OF TODAY'S PRACTICE")

print("{} {}".format("Value of b is :", b))
print("Value of c is :", c)
print(type(a))
print(type(b))
print(type(c))

# List Data Type Practice -> Mutable means can change/update the data

List = ["om", 2, 4.5, 820]
print(List[1])  # Retrieving data
print(List[0:3])

List.append(8)
List.insert(1, "namah shivaya")
List[0] = "OM NAMAH SHIVAYA"  # Updating
del List[1]  # Deleting
print(List)

# Tuple -> Immutable means can't update the data

Tuple = ("OM NAMAH SHIVAYA", 6, 203.98)

print(Tuple[2])

# Dictionary -> Key value pair

Dict = {"a": 1, 5: "b", c: 5, "Key": "Value"}

print(Dict)

Dic = {}
Dic['key'] = "Value"
Dic['Name'] = "BHANU PRAKASH MVS"
Dic['Age'] = 34

print(Dic)
