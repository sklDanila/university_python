# task 1
# def task1(start, end):
#     result = 0
#     while start <= end:
#         if start % 2 == 0 and start % 4 != 0:
#             result += start**2
#     start += 1
#     print(f"Result is {result}")


# task1(int(input("Enter start: ")), int(input("Enter end: ")))


# task2
# def task2(a, b, i):
#     sum = 0
#     while a <= b:
#         if a % i == 0:
#             sum = sum + a
#         a += 1
#     print(sum)


# task2(int(input("Enter start: ")), int(input("Enter end: ")), int(input("Enter i: ")))


# task 3
def task3(broj):
    sum = 0
    for i in broj:
        sum += int(i)
    print(sum)


task3(str(input("Enter broj: ")))
