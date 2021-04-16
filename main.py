 #given the speed of driver, determine the points over his speed limit.
avg_speed = float(input("what is your avarage speed: "))
allowed_speed = float(input("what is your allowed speed: "))
diff = float(avg_speed - allowed_speed)

if diff > 64:
    print("time to go to jail")
elif diff >= 60:
    print("points:12")
elif diff >= 55:
    print("point:11")
elif diff >= 50:
    print("point:10")
elif diff >= 45:
    print("points:9")
elif diff >= 40:
    print("points 8:")
elif diff >= 35:
    print("points 7:")
elif diff >= 30:
    print("points 6:")
elif diff >= 25:
    print("points 5:")
elif diff >= 20:
    print("points 4:")
elif diff >= 15:
    print("points 3:")
elif diff >= 10:
    print("points 2:")
elif diff >= 5:
    print("points 1:")
else:
    print("ok")
