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
        speed = self.axis[1]*100 
        angle = self.axis[2]*90
        
        return [angle, speed]
        
        

       

       
        

    def check_for_exit_click(self):
        for event in pygame.event.get():   # User did something.
            if event.type == pygame.QUIT:  # If user clicked close.
                self.done = True           # Flag that we are done so we exit this loop.
                pygame.quit()              # exit pygame

                

if __name__ == '__main__':

    my_controller = controller()
    while True:
        
        
        my_controller.update_values()
        print(my_controller.get_speed_angle())
    
        #print(my_controller.axis)





### -------- Main Program Loop -----------
##while not done:
##    #
##    # EVENT PROCESSING STEP
##    #
##    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
##    # JOYBUTTONUP, JOYHATMOTION
##
##
##    # DRAWING STEP
##    #
##    # First, clear the screen to white. Don't put other drawing commands
##    # above this, or they will be erased with this command.
##    screen.fill(WHITE)
##    textPrint.reset()
##
##    # Get count of joysticks.
##    joystick_count = pygame.joystick.get_count()
##
##    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
##    textPrint.indent()
##
##    # For each joystick:
##    
##    # Usually axis run in pairs, up/down for one, and left/right for
##    # the other.
##    
##    textPrint.tprint(screen, "Number of axes: {}".format(axes))
##    textPrint.indent()
##
##
##    
##    textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
##    textPrint.unindent()
##
##    
##    textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
##    textPrint.indent()
##
##    
##        textPrint.tprint(screen,
##                         "Button {:>2} value: {}".format(i, button))
##    textPrint.unindent()
##
##    hats = joystick.get_numhats()
##    textPrint.tprint(screen, "Number of hats: {}".format(hats))
##    textPrint.indent()
##
##    # Hat position. All or nothing for direction, not a float like
##    # get_axis(). Position is a tuple of int values (x, y).
##    for i in range(hats):
##        hat = joystick.get_hat(i)
##        textPrint.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
##    textPrint.unindent()
##
##    textPrint.unindent()
##
##    #
##    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
##    #
##
##    # Go ahead and update the screen with what we've drawn.
##    pygame.display.flip()
##
##    # Limit to 20 frames per second.
##    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.

