from nose2.events import Plugin
from tests.ReqTracer import Requirements



class RequirementTestPrinting(Plugin):
    configSection = 'requirementtestprinting'


    def __init__(self):
        with open("ReqTestOutput.txt", 'w') as f:
            for key, item in Requirements.items():
                f.write('{0} - {1} - {2}'.format(key, item.req_text, item.func_name))
              
   
