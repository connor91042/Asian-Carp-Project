from pi_hat_controller import pi_hat
from controller_input import controller

hat = pi_hat()
my_controller = controller()
my_controller.update_values()

while True:
    angle,speed = my_controller.get_speed_angle()

    hat.update_servo(angle)
    hat.ramp_thruster(speed)
    
    
