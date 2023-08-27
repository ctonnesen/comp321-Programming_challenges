start=input()
end=input()

start_hour=int(start.split(":")[0])
start_minute=int(start.split(":")[1])
start_second=int(start.split(":")[2])
end_hour=int(end.split(":")[0])
end_minute=int(end.split(":")[1])
end_second=int(end.split(":")[2])

hours=end_hour-start_hour
if hours<0:
    hours = 24-abs(hours)
hours = ""+hours
minute=end_minute-start_minute
if minute<0:
    minute = 60-abs(minute)
second=end_second - start_second
if second<0:
    second = 60-abs(second)
print(f"{hours}:{minute}:{second}")