# IF Condition

# # Greeting based on time
# time = 12
# if time < 12:
#     print("Good Morning !!!")
# elif time == 12:
#     print("Good Noon !!!")
# elif 12 < time < 16:
#     print("Good After Noon !!!")
# elif 16 <= time <= 20:
#     print("Good Evening !!!")
# elif 20 < time <= 24:
#     print("Good Night !!!")
# else:
#     print("The time entered is NOT correct. Please check and enter the time in between 0 to 24")
#
# print("Out of IF LOOP")
#
# # FOR Loop
# print("***** FOR LOOP *****")
# data = ["OM NAMAH SHIVAYA", 10, 4.5]
# for i in data:
#     print(i * 2)
# temp = 0
#
# for i in range(6):
#     temp = temp + i
# print(temp)
#
# print("********")
# for a in range(1, 23, 3):
#     print(a)

# WHILE Loop

a = 10
while a > 0:
    if a == 7:
        a = a - 1
        continue
    if a == 0:
        break
    print(a)
    a = a - 1
