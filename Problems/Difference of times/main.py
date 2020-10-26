# put your python code here
hours = int(input())
minutes = int(input())
seconds = int(input())
hours_second = int(input())
minutes_second = int(input())
seconds_second = int(input())
first_time = (hours * 3600) + (minutes * 60) + seconds
second_time = (hours_second * 3600) + (minutes_second * 60) + seconds_second
print(second_time - first_time)