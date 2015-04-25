"""
Orc simulator thingamajig
"""


import logging

logger = logging.getLogger(__name__)



class CheckOrc(object):

    def __init__(self, values=None, variations=None):
        self.values = values
        self.is_secure = False
        self.variations = variations
       
        
        
         
    def list_of_orcs(self):
        variations['Light'] = 1
        variations['Uruk-Hai'] = 2
        variations['Gundabad'] = 3
        variations['Possesed'] = 4
        variations['Phantom'] = 5
        variations['Berserker'] = 6
        variations['Sapper'] = 7
        variations['Infiltrator'] = 8
        

    def remove_an_orc (self, variations):
        x = raw_input("Enter orc type you'd like to remove: ")
        variations.remove(x)
        
    def user_input(self, user_string):
        user_string = raw_input("Enter a command: ")
        if user_string == 'x':
            exit()
        if user_string == '?':
            print("Options: ")
            #code that would display options

       
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
       
    
    
