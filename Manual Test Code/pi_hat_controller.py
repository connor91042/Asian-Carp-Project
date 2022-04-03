import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
from time import sleep



class pi_hat():

    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA) #init i2c
        self.hat = adafruit_pca9685.PCA9685(self.i2c)   #init hat
        self.hat.frequency = 50                    #freq in hertz
        self.kit = ServoKit(channels=16)           #init hat shit
        self.thruster = self.hat.channels[0]            #set thruster channel
        self.servo = self.hat.channels[8]               #set servo channel

        self.thruster_percent = 0
        
    def update_servo(self, angle):
        #this method updates the servo's duty cycle
        duty = angle*((.13-.02)/180) + .077 
        
        _16_bit_value = int(float(duty)*(65535))
        #print (_16_bit_value)
        
        self.servo.duty_cycle = _16_bit_value
        # RANGE .02 to .13 
        # CENTERED 0.077

    def update_thruster(self, percent):
        
        #this method updates the thruster percent
        #hysterisis 
        
        
        duty = ((10.7 - 4.25)/200)*float(percent) + 7.7

        if 7.5 < duty < 7.9: #add hysteris for the stop
            duty = 7.7
            
        duty = duty/100
        
        
        _16_bit_value = int(duty*65535)
        
        self.thruster.duty_cycle = _16_bit_value

    def ramp_thruster(self, setpoint):
        #this function ramps the thruster value
        ramp_slope = 35 #percent/sec
        
        diff = (setpoint - self.thruster_percent) #error in value
        time_step = .01
        
        if abs(diff) <= (ramp_slope*time_step): #if thruster setpoint is close to setpoint  
            self.thruster_percent = setpoint #set ouptut to setpoint
            
        elif diff > 0: #ramp up
            sleep(time_step) #change in t is 100ms
            
            self.thruster_percent = self.thruster_percent + ramp_slope*time_step
            
        elif diff < 0: #ramp down
            sleep(time_step)  #change in t is 100ms
            self.thruster_percent = self.thruster_percent - ramp_slope*time_step
            
        self.update_thruster(self.thruster_percent) #update 
    
        
            
        
        
        

if __name__ == '__main__':

    hat = pi_hat()
    
    while True:
        set_point = 50
        hat.ramp_thruster(set_point)
        if hat.thruster_percent == set_point:
            break
        
    while True:
        set_point = 0
        hat.ramp_thruster(set_point)
        if hat.thruster_percent == set_point:
            break

        
##    hat.update_servo(0)
##    hat.update_thruster(0)

    
