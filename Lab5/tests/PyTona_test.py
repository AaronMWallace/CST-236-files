from ReqTracer import requirements
import pyTona
from pyTona import answer_funcs
import mock
from mock import patch
from pyTona.main import Interface
import unittest
import time

class pyTona_testing(unittest.TestCase):
    def setUp(self):
        self.obj = Interface()
        self.obj2 = answer_funcs   
     
    @requirements(['#0003'])
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

    @requirements(['#0006', '#0032'])
    def test_90_percent(self):
        #The word 'many' has been replaced with 'vany'
        start = time.clock()
        ret = self.obj.ask("How vany seconds since?")
        proc_time = time.clock() - start
        self.assertLess(proc_time, 0.005)
        
        self.assertEqual(ret, "42 seconds")

    @requirements(['#0009'])
    def test_no_valid_match(self):
        ret = self.obj.ask("Where is my precious?")
        self.assertEqual(ret, "I don't know, please provide the answer")

    @requirements(['#0007', '#0017'])
    def test(self):
        ret = self.obj.ask("What is 5280 feet in miles?")
        self.assertEqual(ret, "1.0 miles")

        self.assertRaises(Exception, self.obj.ask, "What is 5280 6 feet in miles?")
        
    @requirements(['#0012'])
    def test_teach(self):
        ret = self.obj.teach()
        self.assertEqual(ret, 'Please ask a question first')
        
    @requirements(['#0013'])
    def test_teach2(self):
       
        self.obj.ask("Who invented Python?")
        ret = self.obj.teach("Guido Rossum(BDFL)")
        self.assertEqual(ret, "I don't know about that. I was taught differently")

    def test_teach3(self):
         self.obj.ask("Who inventet Python?")
         self.obj.teach("Guido Rossum(BDFL)")
         
    @requirements(['#0014', '#0015', '#0031'])
    def test_add_answer(self):
       self.obj.ask("Why don't you understand me?")
       
       start = time.clock()
       self.obj.correct("Because you do not kneel before your Dark Queen")
       proc_time = time.clock() - start
       self.assertLess(proc_time, 0.005)
       
       ret = self.obj.ask("Why don't you understand me?")
       self.assertEqual(ret, 'Because you do not kneel before your Dark Queen')

    @requirements(['#0016'])
    def test_correct_response1(self):
        ret = self.obj.correct("Guido Rossum(BDFL)")
        self.assertEqual(ret, 'Please ask a question first')

    @requirements(['#0019'])
    def test_correct_responses2(self):   
        ret = self.obj.ask("Who invented Python?")
        self.assertEqual(ret, "Guido Rossum(BDFL)")

    @requirements(['#0020'])
    def test_correct_responses3(self):
        ret = self.obj.ask("Why don't you understand me?")
        self.assertEqual(ret, "Because you do not speak 1s and 0s")

    @requirements(['#0021'])
    def test_correct_responses3(self):
        ret = self.obj.ask("Why don't you shutdown?")
        self.assertEqual(ret, "I'm afraid I can't do that Aaron")
        #Note: Requirement 21 will vary from computer to computer
        
    @requirements(['#0022'])
    def test_correct_responses4(self):
        ret = self.obj.ask("Where am I?")
        self.assertEqual(ret, "Unknown")

    @requirements(['#0023'])
    def test_correct_responses5(self):
        ret = self.obj.ask("Where are you?")
        self.assertEqual(ret, "Unknown")

    @mock.patch('subprocess.Popen')
    def test_get_git_branch(self, mock_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ['test']}
        process_mock.configure_mock(**attrs)
        mock_popen.return_value = process_mock
        self.obj2.get_git_branch()
        self.obj2.get_git_url()

    @requirements(['#0024', '#0026'])
    @mock.patch('socket.socket')
    def test_get_other_users(self, mock_sock):
        m = mock_sock.return_value
        m.connect.return_value = None
        m.send.return_value = None
        m.recv.return_value = 'Frank$Joe$Bubba'
        ret = self.obj.ask("Who else is here?")
        self.assertEqual(ret, ['Frank', 'Joe', 'Bubba'])

    @requirements(['#0027'])
    def test_correct_responses6(self):
        ret = self.obj.ask("Who else is here?")
        self.assertEqual(ret, "IT'S A TRAAAPPPP")

    @requirements(['#0029'])
    def test_correct_responses7(self):
        ret = self.obj.ask("What is the 5 digit of the Fibonacci sequence?")
        self.obj2.seq_finder.stop()
        self.obj2.seq_finder = None
        if ret == "Thinking...":
            self.assertEqual(ret, 'Thinking...')
            
        elif ret == "One second":
            self.assertEqual(ret, 'One second')
            
        else:
            self.assertEqual(ret, 'cool your jets')

    @requirements(['#0030'])      
    def test_add_a_million_answers(self):
        start = time.clock()
        count = 0
        while count < 1000000:
            self.obj._Interface__add_answer("This is an answer")
            count += 1

        proc_time = time.clock() - start
        self.assertLess(proc_time, 60)

    @requirements(['#0028','#0033','#0034'])
    def test_speed_of_fibonacci(self):
        idx = 0
        start = time.clock()
        self.obj.ask("What is the 5 digit of the Fibonacci sequence?")
        while len(self.obj2.seq_finder.sequence) < 1000:
            ret = self.obj.ask("What is the 5 digit of the Fibonacci sequence?")
            idx += 1

        proc_time = time.clock() - start

        self.obj2.seq_finder.stop()
        self.assertEqual(len(self.obj2.seq_finder.sequence), 1000)
        self.obj2.seq_finder = None
        
        self.assertLess(proc_time, 60)
        
        self.assertEqual(ret, 5)
        
    @requirements(['#0035'])
    def test_speed_of_collatz(self):
        start = time.clock()
        self.obj.ask("How many steps will the Collatz pattern take to reduce 15 to one?")
        self.obj2.col_seq_builder.stop()

        proc_time = time.clock() - start
        self.assertLess(proc_time, 60)
     
         

    @requirements(['#0036'])
    def test_hard_drive_read_and_write(self):
        start = time.clock()
        ret = self.obj.ask("How many viruses do I have?")
        
        proc_time = time.clock() - start
        self.assertLess(proc_time, 0.005)

        if ret == "No Viruses Detected. You\'re safe!":
            self.assertEqual(ret, 'No Viruses Detected. You\'re safe!')
            
        elif ret == "On!y a fe% vi&us#s. Sho^ld 8e ok@y.":
            self.assertEqual(ret, 'On!y a fe% vi&us#s. Sho^ld 8e ok@y.')
            
        else:
            self.assertEqual(ret, '#3lP M5!! V!Ru$*s #ve?yWhE46!')

    @requirements(['#0037'])
    def test_rand_generator(self):
        start = time.clock()
        self.obj.ask("How about you a generate 500 cell long sequence of numbers between one and five?")
        self.obj2.rand_seq.stop()
        proc_time = time.clock() - start

        self.assertLess(proc_time, 0.05)
        
    #requirements not covered: #0001, #0010, #0018, #0026
      
        
