#!/usr/bin/env python3

# ===================================
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# ===================================


import time
import math
import options

from threading import Thread


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

    # ΔL1, ΔL2 to steps
    L1_steps = 5
    L2_steps = 6

    if __name__ == "__main__":
        L1_process = Thread(
            target=m1.motor_go(
                False,
                "Half",
                round(((360 * dL1) / 2 * math.pi) / options.deg_steps),
                speed,
                False,
                0.05,
            )
        )
        L2_process = Thread(
            target=m2.motor_go(
                True,
                "Half",
                round(((360 * dL2) / 2 * math.pi) / options.deg_steps),
                speed,
                False,
                0.05,
            )
        )

        L1_process.start()
        L2_process.start()

        L1_process.join()
        L2_process.join()
