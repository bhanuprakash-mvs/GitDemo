file = open('Test.txt')
# print(file.read(7))
# print(file.readline())  # readline reads single line at a time
# print(file.readline())
# print(file.readline())

for i in file.readlines():  # readlines reads values in a list by applying for loop, we can achieve reading entire data
    print(i)

file.close()

