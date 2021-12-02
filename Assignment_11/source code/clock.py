import time
time_hour = int(input("What is the current hour?"))
time_minute = int(input("What is the current minute?"))
time_second = int(input("What is the current second?"))
am_pm = input("Is it AM or PM?")
seconds = time_second
minutes = time_minute
hour = time_hour
while True:
    seconds += 1
    time.sleep(1)
    if(seconds == 60):
        minutes += 1
        seconds -= 60
    print(hour, ':',minutes, ':', seconds, am_pm)







