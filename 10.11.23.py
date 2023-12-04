import math

# def taxi(killometers):
#     cijena = 1 + (killometers * 0.5)
#     print(f"Cijena za taxi je {cijena}")


# taxi(int(input()))


# def books(price, sale):
#     finish_price = price * (1 - sale / 100)
#     print(f"Finish price of book is {finish_price}")


# books(int(input("Enter price: ")), int(input("Enter sale: ")))


# def game(start_price):
#     finish_price = (start_price * 1.1) * 0.9
#     print(f"Finish price of game is {finish_price}")

# game(int(input("Enter start price: ")))


# def numbers(number):
#     sum = 0
#     if len(number) == 3:
#         for i in number:
#             sum += int(i)
#         print(sum)
#     else:
#         print("Enter three-degit number")


# numbers(str(input()))


# def three_digits(number):
#     sum = 0
#     mot = 1
#     if len(number) == 3:
#         for i in number:
#             sum += int(i)
#         for i in number:
#             mot = mot * int(i)
#         print(mot - sum)
#     else:
#         print("Enter three-degit number")


# three_digits(str(input()))


# def four_digits(number):
#     sum = 0
#     if len(number) == 4:
#        first = number // 1000
#        last = number % 10
#        print(math.pow(first, 2) + math.pow(last, 2))
#     else:
#         print("Enter three-degit number")


# four_digits(int(input()))


# def students(N, K, p1, p2):
#     total = (K * p2 + (N - K) * p1) / N
#     print(f"Total students {round(total, 2)}")


# students(int(input()), int(input()), float(input()), float(input()))
