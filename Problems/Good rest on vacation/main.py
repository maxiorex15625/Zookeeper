# put your python code here
duration = int(input())
food_cost = int(input())
one_way_ticket = int(input())
hotel_cost = int(input())
print((food_cost * duration) + (one_way_ticket * 2) + hotel_cost * (duration - 1))