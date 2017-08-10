from microbit import*

power = 0
while True:
    while power < 1023:
        pin6.write_analog(power)
        power += 1

    while power > 0:
        pin6.write_analog(power)
        power -=1
