from microbit import *

Duty = 0
CountUp = True

while True:
    if CountUp:
        Duty += 1
        pin8.write_analog(Duty)
        sleep(10)
        if Duty == 1023:
            CountUp = False

    if not CountUp:
        Duty -= 1
        pin8.write_analog(Duty)
        sleep(10)
        if Duty == 0:
            CountUp = True
