"""
Orc simulator thingamajig
"""


import logging

logger = logging.getLogger(__name__)

EXIT_STAND_IN = "The program will now exit."
OPTIONS_DISPLAY = "Options: 'x' will exit the program. '?' will display the options."

class CheckOrc(object):

    def __init__(self, values=None, variations=None):
        self.values = values
        self.is_secure = False
        self.variations = ['Light', 'Uruk-Hai', 'Gundabad', 'Possesed', 'Phantom', 'Berserker', 'Sapper', 'Infiltrator']
      
    
    def remove_an_orc(orc_type):
        #x  = raw_input("Enter orc type you'd like to remove: ")
        self.variations.remove(orc_type)
        
    def user_input(self, user_string):
        #user_string = raw_input("Enter a command: ")
        if user_string == 'x':
            return EXIT_STAND_IN
        elif user_string == '?':
            return OPTIONS_DISPLAY

       
    def orc_distance(self, orc_location=None, perimiter=None):
        orc_dis = (perimiter - orc_location)
        orc_vel = 1 #by default we'll say these orcs are all fat and slow
                    # so, they only move one unit at a time.
        print "Orc is %d units away!" % orc_dis
        print "Orc is approaching at %d 'units' per second!" % orc_vel
    
    def check_for_breach(self, orc_location=None, perimiter=None):
        if orc_location > perimiter:
            logger.info('Perimiter Breached!')
        else:
            self.is_secure = True
        logger.info('Perimiter is secure.')
       
    
    
