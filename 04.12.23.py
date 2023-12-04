def task1(string):
    proizvod = 1
    for ch in string:
        if ch.isdigit():
            proizvod *= int(ch)

    print(f"Proizvod numbers: {proizvod}")


task1(str(input("Enter string: ")))
