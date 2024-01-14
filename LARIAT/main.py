#!/usr/bin/env python3

# ===================================
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# ===================================


import time
import math
import options

# from multiprocessing import Process


##### Setup #####
GPIO.setmode(GPIO.BCM)
m1 = RpiMotorLib.A4988Nema(options.m1_dir_pin, options.m1_step_pin, (-1, -1, -1))
m2 = RpiMotorLib.A4988Nema(options.m2_dir_pin, options.m2_step_pin, (-1, -1, -1))


##### Main #####
L1_cur = options.m1_default_length
L2_cur = options.m2_default_length


def goto(x: float, y: float, speed: float = 0.00125):
    if x > options.motor_spacing or y > options.motor_height:
        raise ValueError("Invalid coordinates")

    global L1_cur, L2_cur  # Declare these as global variables

    # Calculate L1, L2
    L1 = math.sqrt((x) ** 2 + (options.motor_height - y) ** 2)
    L2 = math.sqrt((options.motor_spacing - x) ** 2 + (options.motor_height - y) ** 2)

    # Calculate ΔL1, ΔL2
    dL1 = L1 - L1_cur
    dL2 = L2 - L2_cur

    # Set L1, L2 to current lenghts
    L1_cur = L1
    L2_cur = L2


def home():
    input("Start homing, press enter...")

    GPIO.output(options.m1_en_pin, GPIO.HIGH)
    input("Move left motor to homing mark, press enter to continue...")
    GPIO.output(options.m1_en_pin, GPIO.LOW)

    GPIO.output(options.m2_en_pin, GPIO.HIGH)
    input("Move left motor to homing mark, press enter to continue...")
    GPIO.output(options.m2_en_pin, GPIO.LOW)
