'''
    Blaine Booher
    An example class.
'''

class myclass(object):
    def __init__(self, name):
        ''' Initialization Routine '''
        self.name=name
        print "my name is %s" % name
        
    def reverse(self):
        ''' A simple helper function '''
        x = self.name
        x.reverse()
        print "my reversed name is: %s" % x
