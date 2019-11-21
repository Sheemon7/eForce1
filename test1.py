#!/usr/bin/python3
​
import cv2
import numpy as np
import RPi.GPIO as GPIO
import wiringpi
​
import time
import sys

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

Kp = 1000
Ki = 100
Kd = 10000
offset = 50
integral = 0
lastError = 0
derivative = 0
measuring_time = False
powerC = 0

# -----------------------------------------------------------

wiringpi.digitalWrite(MOTOR_DIR_GPIO, 0) #forward

while True:
    LightValue = 0  # read light sensor...value
    if LightValue < 5:
        if not measuring_time:
            start_time = time.time()
            measuring_time = True
        elapsed_time = time.time() - start_time

    else:
        measuring_time = False

    if elapsed_time >= 3:  # if lost line, find it
        while LightValue <= 5:
            powerC = 5
            powerA = 30
            powerB = 30

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
