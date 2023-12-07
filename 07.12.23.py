# task1
"""
list = [2, 4, -4, -2, -5, 7]

sum = 0
for element in list:
    if element < 0 and element % 2 == 0:
        sum += element * (-1)
print(sum)
"""
# task2
"""
i = 0
list22 = []
for i in range(5):
    list22.append(int(input(f"Enter {i+1} element of list: ")))
max = int(input("Enter the maximum number: "))
count = 0
for element in list:
    if element < max:
        count += 1
print(count)
"""

# task3
"""
i = 0
prices = []
for i in range(5):
    prices.append(int(input(f"Enter {i+1} price of list: ")))

sale = int(input("Enter percent of sale: "))
sum1 = 0
sum2 = 0
for element in prices:
    sum1 += element
    sum2 += element - (element * sale / 100)

print(f"Razlika je {sum1- sum2}")
"""

# task4

i = 0
peoples = []
for i in range(10):
    peoples.append(int(input(f"Enter count of people in {i+1} day: ")))

max = 0
for day in peoples:
    if day > 0:
        max = day
p = peoples.index(max)
print(f"Max people in {p + 1} day")
