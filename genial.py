from gpiozero import Button, PWMLED
from signal import pause
from random import randint
from time import sleep

red_led = PWMLED(23)
blue_led = PWMLED(25)
green_led = PWMLED(17)
yellow_led = PWMLED(22)

red_button = Button(18, pull_up=True)
blue_button = Button(24, pull_up=True)
green_button = Button(4, pull_up=True)
yellow_button = Button(27, pull_up=True)
halt_button = Button(26, pull_up=True)

l = 1
numbers = [0]
print('Level 1!')

r = randint(1, 4)
numbers.append(r)

while True:
    sleep(2)
    gamer = [0]
    for n in numbers:
        if n == 1:
            red_led.on()
            sleep(1)
            red_led.off()
        if n == 2:
            blue_led.on()
            sleep(1)
            blue_led.off()
        if n == 3:
            green_led.on()
            sleep(1)
            green_led.off()
        if n == 4:
            yellow_led.on()
            sleep(1)
            yellow_led.off()

    while True:
        if red_button.is_pressed:
            red_led.on()
            if 1 != gamer[-1]:
                gamer.append(1)
        else:
            red_led.off()
        if blue_button.is_pressed:
            blue_led.on()
            if 2 != gamer[-1]:
                gamer.append(2)
        else:
            blue_led.off()
        if green_button.is_pressed:
            green_led.on()
            if 3 != gamer[-1]:
                gamer.append(3)
        else:
            green_led.off()
        if yellow_button.is_pressed:
            yellow_led.on()
            if 4 != gamer[-1]:
                gamer.append(4)
        else:
            yellow_led.off()
        if halt_button.is_pressed:
            break

    if gamer == numbers:
        red_led.pulse()
        blue_led.pulse()
        green_led.pulse()
        yellow_led.pulse()
        print('CONGRATULATIONS! YOU BEAT IT!')
        l += 1
        print('Level up! Level {}!'.format(l))
        sleep(2)
        red_led.off()
        blue_led.off()
        green_led.off()
        yellow_led.off()
        while r == numbers[-1]:
            r = (randint(1, 4))
        numbers.append(r)
    else:
        red_led.pulse()
        print('SORRY, WRONG SEQUENCE!')
        print('Let`s try level {} again!'.format(l))
        sleep(2)
        red_led.off()
    a = ' '
    if a not in 'YN':
        a = input('Do you want to continue playing? [Y/N]').strip().upper()
    if a in 'N':
        print('THANK YOU FOR PLAYING GENIAL!')
        sleep(1)
        break