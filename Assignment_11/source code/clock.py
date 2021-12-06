import time

class Clock(time):

    def __init__():

        while True:
            seconds = time_second
            minutes = time_minute
            hour = time_hour
            seconds += 1
            time.sleep(1)

    def tick(second, minutes, hour):

        if(seconds == 60):
            minutes += 1
            seconds -= 60

        if(minutes == 60):
            hour += 1
            minutes -= 60

        if(hour == 13):
            hour -= 12

        print(hour, ':',minutes, ':', seconds, am_pm)

    def timer(time_hour, time_minute, time_second, am_pm):
        time_hour = int(input("What is the current hour?"))
        time_minute = int(input("What is the current minute?"))
        time_second = int(input("What is the current second?"))
        am_pm = input("Is it AM or PM? ")


        def get_tick():
            while(seconds % 2 == 0):
                print(tick)



time_hour = int(input("What is the current hour?"))
time_minute = int(input("What is the current minute?"))
time_second = int(input("What is the current second?"))
am_pm = input("Is it AM or PM? ")







