from microbit import*

power = 0

while True:
    while power < 1023:
        power += 1
        pin0.write_analog(power)
        sleep(10)
        
    while power > 0:
        power -= 1
        pin0.write_analog(power)
        sleep(10)

