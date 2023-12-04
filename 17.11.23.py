import math

# task 1
# def tests(m1, p1, m2, p2):
#     if m1 + p1 + m2 + p2 <= 200:
#         if m1 + p1 > m2 + p2:
#             print("Win 1st student")
#         elif m1 + p1 == m2 + p2:
#             if p1 > p2:
#                 print("Win 1st student")
#             elif p1 == p2:
#                 print("Win nobody")
#             else:
#                 print("Win 2nd student")
#         else:
#             print("Win 2nd student")
#     else:
#         print("Enter right points")


# tests(
#     int(input("Enter points for math 1st student: ")),
#     int(input("Enter points for programming 1st student: ")),
#     int(input("Enter points for math 2nd student: ")),
#     int(input("Enter points for programming 2nd student: ")),
# )


# task 2
# def points(score):
#     if score <= 5.0 and score >= 1:
#         if score > 4.5:
#             print("Your mark perfect")
#         elif score < 4.5 and score >= 3.5:
#             print("Your mark good")
#         elif score < 3.5 and score >= 2.5:
#             print("Your mark not good")
#         elif score < 2.5 and score >= 2:
#             print("Your mark bad")
#         elif score < 2:
#             print("You mustnt go to school")
#     else:
#         print("Enter right mark")


# points(float(input()))

# task 3
# def window(x1, y1, x2, y2, x3, y3, x4, y4):
#     if x2 - x1 == x4 - x3 and y1 - y2 == y3 - y4:
#         print("Good size")
#     else:
#         print("Bad size")


# window(
#     int(input("Enter x1 window(gornja lijeva): ")),
#     int(input("Enter y1 window(gornja lijeva): ")),
#     int(input("Enter x2 window(donja desna): ")),
#     int(input("Enter y2 window(donja desna): ")),
#     int(input("Enter x3 oblika(gornja lijeva): ")),
#     int(input("Enter y3 oblika(gornja lijeva): ")),
#     int(input("Enter x4 oblika(donja desna): ")),
#     int(input("Enter y4 oblika(donja desna): ")),
# )

# task 4
# def darts(radius, x_center, y_center, x_strela, y_strela):
#     if x_strela < x_center + radius and x_strela > x_center - radius:
#         if y_strela < y_center + radius and y_strela > y_center - radius:
#             print("Win")
#         else:
#             print("Loser")
#     else:
#         print("Loser")


# darts(
#     int(input("Enter radius: ")),
#     int(input("Enter coordinate x of center darts: ")),
#     int(input("Enter coordinate y of center darts: ")),
#     int(input("Enter coordinate x of strela: ")),
#     int(input("Enter coordinate y of strela: ")),
# )


# def darts(radius, x_center, y_center, x_strela, y_strela):
#     if (
#         math.sqrt(
#             math.pow((x_strela - x_center), 2) + math.pow((y_strela - y_center), 2)
#         )
#         <= radius
#     ):
#         print("Win")
#     else:
#         print("Loser")


# darts(
#     int(input("Enter radius: ")),
#     int(input("Enter coordinate x of center darts: ")),
#     int(input("Enter coordinate y of center darts: ")),
#     int(input("Enter coordinate x of strela: ")),
#     int(input("Enter coordinate y of strela: ")),
# )


# task 5
def mrav(x1_table, y1_table, x2_table, y2_table, x_mrav, y_mrav):
    if (x_mrav == x1_table or x_mrav == x2_table) and (
        y1_table < y_mrav < y2_table or y1_table > y_mrav > y2_table
    ):
        print("Good")
    elif (y_mrav == y1_table or y_mrav == y2_table) and (
        x1_table < x_mrav < x2_table or x1_table > x_mrav > x2_table
    ):
        print("Good")
    else:
        print("bad")


# task 6
def month(month):
    if month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("Oktober")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")


month(int(input("Enter number of month: ")))
