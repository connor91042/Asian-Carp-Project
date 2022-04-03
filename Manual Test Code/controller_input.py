import pygame


# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')


class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

class controller(): #inherit TextPrint's methods

    def __init__(self):
        pygame.init() #begin pygame main loop

        screen = pygame.display.set_mode((500, 700))  # Set the width and height of the screen (width, height).
        pygame.display.set_caption("Controller info") # Set screen name

        
        
        
        clock = pygame.time.Clock()                   # Used to manage how fast the screen updates.

        self.done = False                             # Loop until the user clicks the close button.
        pygame.joystick.init()                        # Initialize the joysticks.
        
        self.textPrint = TextPrint()                  # Get ready to print.

        self.joystick = pygame.joystick.Joystick(0)   #select the joystick object
        self.joystick.init()                          #init joystick object


        self.axis = []                                #init axis values
        axes = self.joystick.get_numaxes()
        
        for i in range(axes):
            self.axis.append(self.joystick.get_axis(i))

        self.buttons = []
        buttons = self.joystick.get_numbuttons()           #init buttons
        for i in range(buttons):
            self.buttons.append(self.joystick.get_button(i)) 
        
        
    
    def update_values(self):
        #this method updates the joystick value stakes.
        
        for i in range(len(self.axis)):                          #update joystick
            self.axis[i] = self.joystick.get_axis(i)
            


        for i in range(len(self.buttons)):
            self.buttons[i] = self.joystick.get_button(i)        #update buttons

        pygame.event.get()

    def get_speed_angle(self):
        #this gives us a speed and angle control signal
        self.update_values()
        
        speed = self.axis[1]*100 
        angle = self.axis[2]*90
        
        return angle, speed
        
        

       

       
        

    def check_for_exit_click(self):
        for event in pygame.event.get():   # User did something.
            if event.type == pygame.QUIT:  # If user clicked close.
                self.done = True           # Flag that we are done so we exit this loop.
                pygame.quit()              # exit pygame

    
    
                

if __name__ == '__main__':

    my_controller = controller()
    while True:
        
        
        my_controller.update_values()
        my_controller.get_speed_angle()
        print(my_controller.buttons)
    
        #print(my_controller.axis)
