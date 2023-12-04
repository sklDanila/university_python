# def task1(string):
#     for ch in string:
#         if ch.isdigit():
#             print(ch, end="")


# task1(str(input("Please enter string: ")))


# def task2(string):
#     for ch in string:
#         if ch in "aeiouy":
#             print(1, end="")
#         else:
#             print(0, end="")


# task2(str(input("Please enter string: ")))


# def task3(string):
#     sum = 0
#     for ch in string:
#         if ch == "1":
#             sum += 1
#         elif ch == "0":
#             sum += 0
#         elif ch == "*":
#             sum -= 1
#     if sum > 0:
#         print(f"You have a good score {sum}")
#     else:
#         print(f"You have a bad score {sum}")


# task3(str(input("Please enter string: ")))


def task4(string):
    for ch in string:
        if int(ch) % 2 == 0:
            print(0, end="")
        elif int(ch) % 2 != 0:
            print(1, end="")


task4(str(input("Please enter string: ")))
