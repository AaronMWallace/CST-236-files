from ReqTracer import requirements
import pyTona
from pyTona import answer_funcs
from mock import patch
from pyTona.main import Interface
import unittest

class testing_goes_here(unittest.TestCase):
    def setUp(self):
        self.obj = Interface()
        self.obj2 = answer_funcs   
        
    @requirements(['#0003', '#0030'])
    def test_ask(self):
        ret = self.obj.ask("Half Life 3 confirmed?")
        self.assertEqual(ret, "Was that a question?")

        self.assertRaises(Exception, self.obj.ask, 7)
        

    @requirements(['#0002', '#0008'])
    def test_ask_again(self):
        ret = self.obj.ask("How many seconds since?")
        self.assertEqual(ret, "42 seconds")
                
        
    @requirements(['#0004'])
    def test_ask_no_question_mark(self):
        ret = self.obj.ask("Who else is here")
        self.assertEqual(ret, "Was that a question?")

    @requirements(['#0006', '#0009'])
    def test_90_percent(self):
        #The word 'many' has been replaced with 'vany'
        ret = self.obj.ask("How vany seconds since?") 
        self.assertEqual(ret, "42 seconds")
        ret = self.obj.ask("Where is my precious?")
        self.assertEqual(ret, "I don't know, please provide the answer")

    @requirements(['#0007', '#0017', '#0031'])
    def test(self):
        ret = self.obj.ask("What is 5280 feet in miles?")
        self.assertEqual(ret, "1.0 miles")

        self.assertRaises(Exception, self.obj.ask, "What is 5280 6 feet in miles?")
        
    @requirements(['#0012', '#0013'])
    def test_teach(self):
        ret = self.obj.teach()
        self.assertEqual(ret, 'Please ask a question first')
        self.obj.ask("Who invented Python?")
        self.obj.teach("Guido Rossum(BDFL)")
        ret = self.obj.teach("Guido Rossum(BDFL)")
        self.assertEqual(ret, "I don't know about that. I was taught differently")

    @requirements(['#0014', '#0015'])
    def test_add_answer(self):
       self.obj.ask("Why don't you understand me?")
       self.obj.correct("Because you do not kneel before your Dark Queen")
       ret = self.obj.ask("Why don't you understand me?")
       self.assertEqual(ret, 'Because you do not kneel before your Dark Queen')

    @requirements(['#0016'])
    def test_correct(self):
        ret = self.obj.correct("Guido Rossum(BDFL)")
        self.assertEqual(ret, 'Please ask a question first')

    @requirements(['#0019','#0020','#0021','#0022','#0023', '#0027','#0029'])
    def test_correct_responses(self):
        ret = self.obj.ask("Who else is here?")
        self.assertEqual(ret, "IT'S A TRAAAPPPP")

        ret = self.obj.ask("Where am I?")
        self.assertEqual(ret, "Unknown")
        
        ret = self.obj.ask("Where are you?")
        self.assertEqual(ret, "Unknown")
        
        ret = self.obj.ask("Who invented Python?")
        self.assertEqual(ret, "Guido Rossum(BDFL)")

        ret = self.obj.ask("Why don't you understand me?")
        self.assertEqual(ret, "Because you do not speak 1s and 0s")

        ret = self.obj.ask("What is the 5 digit of the Fibonacci sequence?")
        self.obj2.seq_finder.stop()
        if ret == "Thinking...":
            self.assertEqual(ret, 'Thinking...')
        elif ret == "One second":
            self.assertEqual(ret, 'One second')
        else:
            self.assertEqual(ret, 'cool your jets')

        ret = self.obj.ask("Why don't you shutdown?")
        self.assertEqual(ret, "I'm afraid I can't do that Aaron")
        #Note: Requirement 21 will vary from computer to computer

    @requirements(['#0024'])
    @patch('pyTona.answer_funcs.get_other_users')
    def test_getting_users(self, MockClass1):
        MockClass1.return_value = "Templeton Peck", "B.A Baracus", "Murdoch", "Col. John 'Hannibal' Smith"
        
        ret = pyTona.answer_funcs.get_other_users()
        self.assertTrue(MockClass1.called)
        self.assertEqual(ret, ("Templeton Peck", "B.A Baracus", "Murdoch", "Col. John 'Hannibal' Smith"))
    
     
            


  #requirements not covered: #0001, #0010, #0018, #0026, #0028








        
