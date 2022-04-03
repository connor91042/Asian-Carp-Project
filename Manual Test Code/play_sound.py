import pygame


class sound_card_():

    def __init__(self):
        
        self.sound_file = 'EngineSoundLoop.mp3' #init sound variable
        self.sound = ''      #init pygame sound variable
        self.channel = ''    #init the sound channel
        pygame.mixer.pre_init(44100,16,2,4096) #freq, size, channels, buffersize
        pygame.mixer.init()

    def play_sound(self):
        #this module plays the sound from the robot
        #pygame.mixer.pre_init(44100,16,2,4096) #freq, size, channels, buffersize
        pygame.mixer.init()
        
        pygame.mixer.music.load(self.sound_file)
        
        pygame.mixer.music.play(-1) #-1 loops forever
        
        
    def mute_sound(self):
        self.channel.set_volume(0)  #mute

    def sound_volume(self, percent):
        #this function sets sound level 0-1
        pygame.mixer.music.set_volume(percent/100)


if __name__ ==  '__main__':
    sound_card = sound_card_()
    sound_card.play_sound()
    sound_card.sound_volume(0)
