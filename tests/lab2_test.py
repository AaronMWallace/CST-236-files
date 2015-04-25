from source.lab2_source import CheckOrc
import logging
import unittest

class PlaceOrc(unittest.TestCase):

        def setUp(self):
                self.obj = CheckOrc(values={'0' : '10'})
                self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

        def test_init(self):
                self.assertEqual(self.obj.values, { '0' : '10'})

        def test_list(self):
                self.obj.list_of_orcs()
                

        def test_remove(self):
                self.obj.remove_an_orc(8)

        def test_with_breach(self):
                self.obj.check_for_breach(orc_location=11, perimiter=10)
                self.assertFalse(self.obj.is_secure)

        def test_user_input(self):
                self.obj.user_input(user_string = 'x')
                self.obj.user_input(user_string = '?')
                

        def test_without_breach(self):
                self.obj.check_for_breach(orc_location=9, perimiter=10)
                self.assertTrue(self.obj.is_secure)

        def test_distance(self):
                self.obj.orc_distance(orc_location=9, perimiter=10)
