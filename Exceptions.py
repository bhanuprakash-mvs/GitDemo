# If want to check for any failures we can use "raise Exception" or "assert()"
# Try and Except block allows to avoid errors for any uncertainty scenario
# finally will run even though some part of code is failed. it can be used to clean up the records.

a = 0

# assert(a == 5)

# if a != 5:
#     raise Exception("Not Matching")

try:
    with open('Tesjsnxt.txt', 'r') as reader:
        scan = reader.readlines()

# except Exception as e:
#     print(e)

except:
    print("the error is")

finally:
    print("end of data")

