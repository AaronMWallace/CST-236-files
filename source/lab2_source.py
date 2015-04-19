"""
Orc simulator thingamajig
"""

import logging

logger = logging.getLogger(__name__)

class CheckOrc(object):

    def __init__(self, values=None):
        self.values = values
        self.is_secure = False

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
       
    
    
