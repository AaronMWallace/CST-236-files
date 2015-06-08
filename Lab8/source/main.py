import inspect
import os

debug_idx = 0

modules = os.listdir('C:\Python27\Lib')

#if ((single_member[0] == '_') and (single_member[1] == '_')):
 #   print "\ndouble underscore detected"

#ret = inspect.isclass(single_member)
#print "\nis class? T/F -> ",ret


idx = 0
while (idx < 2):
    sub_idx = 0
    Value = modules[idx]
    Value = Value.rsplit('.')[0]

    try:
        globals()[Value] = __import__(Value)
        print "Import complete"
    
    except ImportError:
        print modules[debug_idx],"failed to import."
    
    members = inspect.getmembers(Value)
    
    
    while (sub_idx < len(members)):
        temp = [x[0] for x in members]
        single_member = temp[sub_idx]
        ret = inspect.ismethod(single_member)
  
        if ret == True:
            print single_member, "is a class--------------------." 
            sub_idx += 1
        else:
            print single_member, "is NOT a class."
            sub_idx += 1
    idx += 1
    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "




