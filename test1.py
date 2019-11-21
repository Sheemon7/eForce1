#!/usr/bin/python3
​
import cv2
import numpy as np
import RPi.GPIO as GPIO
import wiringpi
​
import time
import sys


def setup_gpios():
    # Setup GPIOs
    wiringpi.wiringPiSetupGpio()

    wiringpi.pinMode(LED_GPIO, wiringpi.GPIO.OUTPUT)
    wiringpi.digitalWrite(LED_GPIO, wiringpi.GPIO.OUTPUT)

    wiringpi.pinMode(MOTOR_SPL_EN_GPIO, wiringpi.GPIO.OUTPUT)

    wiringpi.pinMode(MOTOR_DIR_GPIO, wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(MOTOR_DISABLE_GPIO, wiringpi.GPIO.OUTPUT)

    wiringpi.pinMode(MOTOR_PWM_GPIO, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.pinMode(SERVO_PWM_GPIO, wiringpi.GPIO.PWM_OUTPUT)

    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)

    wiringpi.pinMode(SONIC_ECHO_GPIO, wiringpi.GPIO.INPUT)
    wiringpi.pinMode(SONIC_TRIG_GPIO, wiringpi.GPIO.OUTPUT)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SW_GPIO, GPIO.IN)
    GPIO.add_event_detect(SW_GPIO, GPIO.FALLING, button_pressed, 200)


# Configuration of basic constant
MIN_ANGLE = 80
MAX_ANGLE = 140
​
SPEED = 300
CENTER = MIN_ANGLE + (MAX_ANGLE - MIN_ANGLE) / 2

# Motor supply enable
MOTOR_SPL_EN_GPIO = 10
​
# DC motor PWM GPIO
MOTOR_PWM_GPIO = 12
​
# DC motor direction GPIO
MOTOR_DIR_GPIO = 6
​
# DC motor disable GPIO
MOTOR_DISABLE_GPIO = 19
​
# Servo motor PWM GPIO
SERVO_PWM_GPIO = 13

# -----------------------------------------------------------

# Setup motor
wiringpi.pwmWrite(MOTOR_PWM_GPIO, 0)
wiringpi.digitalWrite(MOTOR_SPL_EN_GPIO, 1)
wiringpi.digitalWrite(MOTOR_DISABLE_GPIO, 0)

# Center wheels
wiringpi.pwmWrite(SERVO_PWM_GPIO, CENTER)

# -----------------------------------------------------------

Kp = 5  # 1000
Ki = 0  # 100
Kd = 0  # 10000
offset = (50 + 261) / 2
integral = 0
lastError = 0
derivative = 0
measuring_time = False
powerC = 0
run = False
first_time = True

# -----------------------------------------------------------

wiringpi.digitalWrite(MOTOR_DIR_GPIO, 0)  # forward
setup_gpios()

while first_time:
    while run:
        if first_time:
            first_time = False
        LightValue = 0  # read light sensor...value
        # if LightValue < 5:
        #     if not measuring_time:
        #         start_time = time.time()
        #         measuring_time = True
        #     elapsed_time = time.time() - start_time
        #
        # else:
        #     measuring_time = False
        #
        # if elapsed_time >= 3:  # if lost line, find it
        #     while LightValue <= 5:
        #         final_turn = CENTER + 15
        #         wiringpi.pwmWrite(SERVO_PWM_GPIO, final_turn)
        #         wiringpi.pwmWrite(MOTOR_PWM_GPIO, SPEED / 8)

        error = LightValue - offset
        integral = integral + error
        derivative = error - lastError
        Turn = Kp * error + Ki * integral + Kd * derivative
        Turn = Turn / 100
        final_turn = CENTER + Turn
        if final_turn < MIN_ANGLE:
            final_turn = MIN_ANGLE
        elif final_turn > MAX_ANGLE:
            final_turn = MAX_ANGLE

        wiringpi.pwmWrite(SERVO_PWM_GPIO, final_turn)
        time.sleep(0.01)

        wiringpi.pwmWrite(MOTOR_PWM_GPIO, SPEED / 4)
        lastError = error


def button_pressed():
    global run
    if not run:
        run = True
    else:
        run = False
