import math
from datetime import datetime

# def koordinate(x1, y1, x2, y2):
#     p = (x2 - x1) * (y2 - y1)
#     o = 2 * (x2 - x1) + 2 * (y2 - y1)
#     print(f"P = {p}, i O =  {o}")


# koordinate(int(input()), int(input()), int(input()), int(input()))


# def euclide_distance(x1, y1, x2, y2):
#     distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
#     print(f"Distance between A i B = {distance}")


# euclide_distance(int(input()), int(input()), int(input()), int(input()))


# def points(x1, y1, x2, y2):
#     x_blago = x2 + 2
#     y_balgo = y2 - 3
#     distance_to_blago1 = math.sqrt(
#         math.pow(x_blago - x1, 2) + math.pow(y_balgo - y1, 2)
#     )
#     distance_to_blago2 = math.sqrt(
#         math.pow(x2 - x1, 2) + math.pow(y1 - y2, 2)
#     ) + math.sqrt(math.pow(x_blago - x2, 2) + math.pow(y_balgo - y2, 2))
#     print(
#         f"coordinate x of Blago is {x_blago}, coordinates y of Blago is {y_balgo}"
#         + "\n"
#         + f"Distance from G to Blago is {distance_to_blago1}"
#         + "\n"
#         + f"Distance 2 from G to Blago is {distance_to_blago2}"
#     )


# points(int(input()), int(input()), int(input()), int(input()))


# def birthday(year_now):
#     current_time = datetime.now()
#     year_born = current_time.year - year_now
#     print(year_born)

# birthday(20)


# def flat(size, location, parking):
#     price = 1200 * (size + location * 5 * size + parking * 10 * location) + 1000
#     print(f"Price of the flat is {price}")


# flat(int(input()), int(input()), int(input()))
