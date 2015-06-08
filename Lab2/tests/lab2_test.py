from source.lab2_source import CheckOrc
import logging
import unittest

class PlaceOrc(unittest.TestCase):

        def setUp(self):
                self.obj = CheckOrc(values={'0' : '10'})
                self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

        def test_init(self):
                self.assertEqual(self.obj.values, { '0' : '10'})

               
        #def test_remove(self):
             #   self.obj.remove_an_orc('Light')

        def test_with_breach(self):
                self.obj.check_for_breach(11, 10)
                self.assertFalse(self.obj.is_secure)

        def test_user_input(self):
                ret = self.obj.user_input('x')
                self.assertEqual(ret, "The program will now exit.")
                
        def test_user_input2(self):
                ret = self.obj.user_input('?')
                self.assertEqual(ret, "Options: 'x' will exit the program. '?' will display the options.")
                

        def test_without_breach(self):
                self.obj.check_for_breach(9, 10)
                self.assertTrue(self.obj.is_secure)

        def test_distance(self):
                self.obj.orc_distance(9, 10)
