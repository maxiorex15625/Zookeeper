money = int(input())
years = 0
while money <= 700000:
    money = money * 1.071
    years += 1
print(years)