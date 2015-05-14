import getpass
import random
import socket
import subprocess
import threading
import time

seq_finder = None
col_seq_builder = None
input_value = None
rand_seq = None

def feet_to_miles(feet):
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch():
    try:
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_git_url():
    try:
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_other_users():
    try:
        host = '192.168.64.3'
        port = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes < 1000:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            self.num_indexes += 1
            time.sleep(.04)

def get_fibonacci_seq(index):
    index = int(index)
    global seq_finder
    if seq_finder is None:
        
        seq_finder = FibSeqFinder()
        seq_finder.start()

    if index > seq_finder.num_indexes:
        value = random.randint(0, 9)
        if value >= 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]


class Collatz(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Collatz, self).__init__(*args, **kwargs)
        self.sequence = []
        self._stop = threading.Event()
        self.num_of_indexes = 0
        
        self.input_value = input_value

               
    def stop(self):
        self._stop.set()

    def run(self):
        while self.input_value != 1:
            if (self.input_value % 2 == 0):
                self.input_value /= 2
                self.sequence.append(self.input_value)
                self.num_of_indexes += 1
            else:
                self.input_value = ((self.input_value * 3) + 1)
                self.sequence.append(self.input_value)
                self.num_of_indexes += 1
       

def get_collatz_seq(user_input):
    
    global input_value
    input_value = int(user_input)
    global col_seq_builder
    if col_seq_builder is None:
        
        col_seq_builder = Collatz()
        col_seq_builder.start()
    return col_seq_builder

def scan_for_virus():
    value = random.randint(0, 13)
    if value >= 9:
        with open("VirusScanResults.txt", 'w') as f:
            f.write("No Viruses Detected. You\'re safe!")
    elif value > 5:
        with open("VirusScanResults.txt", 'w') as f:
            f.write("On!y a fe% vi&us#s. Sho^ld 8e ok@y.")
    else:
        with open("VirusScanResults.txt", 'w') as f:
            f.write("#3lP M5!! V!Ru$*s #ve?yWhE46!")

    with open("VirusScanResults.txt", 'r') as f:
           scan_result = f.readline()
    return scan_result



class random_generator(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(random_generator, self).__init__(*args, **kwargs)
        self.sequence = []
        self._stop = threading.Event()
        self.num_of_indexes = 0
        self.input_num = seq_length
     

               
    def stop(self):
        self._stop.set()

    def run(self):
        while self.num_of_indexes < self.input_num:
            value = random.randint(0, 5)
            self.sequence.append(value)
            self.num_of_indexes += 1
                  

def get_rand_seq(user_num):
    
    global seq_length
    seq_length = int(user_num)
    global rand_seq
    if rand_seq is None:
        
        rand_seq = random_generator()
        rand_seq.start()

    return rand_seq.sequence












































    






                
    
