import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

hat.frequency = 50

thruster = hat.channels[0]

while True:
    percentage_on = input("enter percent: ")
                                              # SAFE OPERATING RANGE: -130 to 140
                                              # STOPPING RANGE: 3 to 11

    duty = (5/200)*float(percentage_on) + 7.5
    duty = duty/100

#    _16_bit_value = int(float(duty)(65535))
    _16_bit_value = int(duty*65535)

    thruster.duty_cycle = _16_bit_value
    print (_16_bit_value)