# print(*range(20))
#
# number = int(input("What is your number?"))
# print(*range(number))

list = [0,1]
# print(*(list*10))

repeat = int(input("How much do u want the list to repeat?:"))

for i in range(1, repeat + 1):
    if i % 2 == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")

