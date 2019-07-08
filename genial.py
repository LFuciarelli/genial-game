from gpiozero import Button, PWMLED
from signal import pause
from random import randint
from time import sleep


def setup():  # Communicates with the GPIO
    global red_led, blue_led, green_led, yellow_led  # The LEDs and buttons must be global variables
    global red_button, blue_button, green_button, yellow_button, halt_button
    red_led = PWMLED(23)  # Declaring the LEDs as PWMLED permits the use of the module .pulse()
    blue_led = PWMLED(25)
    green_led = PWMLED(17)
    yellow_led = PWMLED(22)
    red_button = Button(18, pull_up=True)
    blue_button = Button(24, pull_up=True)
    green_button = Button(4, pull_up=True)
    yellow_button = Button(27, pull_up=True)
    halt_button = Button(26, pull_up=True)


def destroy():  # Turns the LEDs off
    red_led.off()
    blue_led.off()
    green_led.off()
    yellow_led.off()


def numbers():  # Generates a random sequence of numbers from 1 to 4 (1 = red, 2 = blue, 3 = green, 4 = yellow)
    randnum = randint(1, 4)
    while randnum == lights[-1]:
        randnum = (randint(1, 4))
    lights.append(randnum)


def rightseq():  # The sequence of colours generated is showed to the player
    for num in lights:
        if num == 1:
            red_led.on()
            sleep(1)
            red_led.off()
        if num == 2:
            blue_led.on()
            sleep(1)
            blue_led.off()
        if num == 3:
            green_led.on()
            sleep(1)
            green_led.off()
        if num == 4:
            yellow_led.on()
            sleep(1)
            yellow_led.off()


def playerseq():  # When the player turns a LED on, the LED's number is added to the list "player"
    if red_button.is_pressed:
        red_led.on()
        if 1 != player[-1]:
            player.append(1)
    else:
        red_led.off()
    if blue_button.is_pressed:
        blue_led.on()
        if 2 != player[-1]:
            player.append(2)
    else:
        blue_led.off()
    if green_button.is_pressed:
        green_led.on()
        if 3 != player[-1]:
            player.append(3)
    else:
        green_led.off()
    if yellow_button.is_pressed:
        yellow_led.on()
        if 4 != player[-1]:
            player.append(4)
    else:
        yellow_led.off()


def check():  # Checks whether the player turned the right LEDs on or not
    global level
    if player == lights:  # All the colours pulse when the player's sequence is right
        red_led.pulse()
        blue_led.pulse()
        green_led.pulse()
        yellow_led.pulse()
        print('CONGRATULATIONS! YOU BEAT IT!')
        level += 1
        print('Level up! Level {}'.format(level))
        sleep(2)
        red_led.off()
        blue_led.off()
        green_led.off()
        yellow_led.off()
        numbers()  # When the player pass to the next level, one more colour is added to the sequence
    else:
        red_led.pulse()  # The red LED pulse when the player's sequence is wrong
        print('SORRY, WRONG SEQUENCE!')
        print('Let`s try level {} again!'.format(level))
        sleep(2)
        red_led.off()


def game_loop():
    print('Level 1!')
    while True:
        sleep(2)
        rightseq()
        while True:
            playerseq()
            if halt_button.is_pressed:
                break
        check()


while True:  # Main program
    setup()
    lights = [0]  # The list "lights" has to start with 0 because it has to have at least one item assigned to it
    player = [0]  # The list "player" has to start with 0 because it has to be the same as the list "lights"
    level = 1
    try:
        numbers()
        game_loop()
    except KeyboardInterrupt:  # Press Ctrl + C to leave the game
        print('THANK YOU FOR PLAYING GENIAL!')
        destroy()
        break
