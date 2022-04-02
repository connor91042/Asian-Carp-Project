import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

hat.frequency = 50

#kit.servo[0].angle = 18
led_channel = hat.channels[8]
#led_channel.duty_cycle = 0x1388

while True:
    duty = input("enter duty cycle: ")  #example 7.5

    _16_bit_value = int(float(duty)*(65535))
    print (_16_bit_value)

    led_channel.duty_cycle = _16_bit_value
    # RANGE .02 to .13 
    # CENTERED 0.077