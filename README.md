# LARIAT - A Direct-Driven Cable Robot
### Laser Analysis Robotic Instrument for Amplitude Tracking

## Overview

This Python script provides basic functionality for controlling two stepper motors (m1 and m2) using the RPiMotorLib library on a Raspberry Pi. The motors are configured as A4988 NEMA motors and connected to the Raspberry Pi GPIO pins as per the options defined in the `options.py` file.

## Setup

1. Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```

2. Connect the stepper motors to the specified GPIO pins in the `options.py` file.

3. Connect the motor wires according to the provided information on motor wire colors.

## Usage

### Motor Wire Mapping

**Coil A:**
- Yellow: Green
- Black: Black

**Coil B:**
- White: Blue
- Red: Red

### Running the Script

1. Run the script:
    ```bash
    python -i main.py
    ```

2. Follow the instructions to start homing and move the motors to the homing marks.

3. Input coordinates using the `goto(x, y)` function to move the motors to specific positions.

## Important Notes

- Ensure the correct GPIO pin configuration in the `options.py` file.

- Be cautious while moving the motors manually, especially during homing.

- Review the motor wire colors to correctly identify and connect the coils.

- Adjust the `options.py` file as needed for your specific setup (measurements to ensure correct calculations for your system).


## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
