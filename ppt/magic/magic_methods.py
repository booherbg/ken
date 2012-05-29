'''
    Some examples of magic methods
    
    Blaine Booher / Ken Hill 2012
'''

# Here's a basic class
class computer():
    def __init__(self, platform, memory, peripherals=None):
        '''
            This is our first magic method...
            __init__ is called every time ani nstance of this class
            is created by the interpreter
            
            platform is a string, like 'x86'
            memory is an integer, like 512
            peripherals is a list, or nothing. like ['mouse', 'keyboard', 'hard drive']
        '''
        self.platform=platform
        self.memory=memory
        if peripherals is not None:
            self.peripherals=list(peripherals) # force to list since we now implement __setitem__
            
    def __call__(self, memory):
        '''
            Magic method for turning an object into something callable
            
            For this, let's take in number and just add it to our memory, then return it.
            Do something special if we're passed in a string.
            
            see the example for something fun using map()
        '''
        if isinstance(memory, int):
            return self.memory + memory
        else:
            return str(self.memory) + "_" + str(memory)
       
    def __iter__(self):
        '''
            Magic Method: for x in obj: print x
            We can use our peripherals list. We also introduce 'yield'
            
            Yield is just like "return" except that the state of the function is saved
            and the next time the routine is called (aka the next iteration in the for loop)
            and the iteration is continued from where it left off.
        '''
        for p in self.peripherals:
            yield p
            
            

    def __contains__(self, name):
        '''
            Magic method for "does object contain x"
            
            Since we're using our self.peripherals list, simply see if the
            string object is a peripheral. For more complex classes, you 
            could do more interesting comparisons (like going to a database
            or something similar)
        '''
        return name in self.peripherals
            
    def __setitem__(self, number, value):
        '''
            Magic method for saving data based on index like obj[x] = 'hello there'
        '''
        try:
            self.peripherals[number] = value
        except IndexError:
            # called when we're trying to set a value out of range...
            # we can either handle it by increasing the number of values,
            # or just notify the user that we can't make it happen.
            # i choose to make it work.
            n = len(self.peripherals)
            diff = number - n + 1 # how many slots to add to the list
            for i in range(diff):
                self.peripherals.append('empty slot')
            print len(self.peripherals)
            self.peripherals[number] = value
        
    def __getitem__(self, number):
        '''
            Magic method for grabbing data from this object, like obj[x]
            
            Let's use the perhipherals list. 
            computer_obj[2] should return the third (index 2) peripheral in our 
            internal peripheral list.
        '''
        if self.peripherals == None:
            return ''
        elif len(self.peripherals) < number:
            return ''
        else:
            return self.peripherals[number]
        
    def __str__(self):
        '''
            Another magic method. This is called when we wish to 
            print this class. Simply return a string that represents
            a pretty notation for printing
        '''
        return "computer object; platform: %s; memory: %d" % (self.platform, self.memory)
        
    def __repr__(self):
        '''
            Very similar to __str__(). If __str__() does not exist,
            python treats any request to __str__() as a request to
            __repr__().
            
            rule of thumb: __repr__() is for developers, __str__() 
            is for customers.
            
            Some developers try to make repr() return something that
            could be evaluated into an object, like this:
                computer(platform, memory)
                
            So let's do that.
            
            this actually gets called when we don't even print, just type 'c' in interpreter
        '''
        return "computer(platform=\'%s\', memory=%s)" % (self.platform, self.memory)
        
    def __cmp__(self, other):
        '''
            Compare this computer to another instance of a computer.
            ex: computer1 > computer2
            
            We return -1, 0, or 1:
                -1 if this instance is "less than" the other instance
                0  if this instance is "equivalent" to the other instance
                1  if this instance is "greater than" the other instance
            
            For this example, let's compare RAM (self.memory)
        '''
        if self.memory == other.memory:
            return 0 # they're equal!
        elif self.memory < other.memory:
            return -1 # we're smaller than their memory
        else:
            return 1 # we're greater than the other memory
            
if __name__ == "__main__":
    '''
        Technically another magic method. If this file is called
        directly, the __name__ variable will contain the value
        '__main__', otherwise it will be empty. This allows us
        to distinguish between a library and an application
    '''
    mac = computer('mac', 512)
    pc = computer('x86', 1024)
    print mac # call __str__()
    print pc  # call __str__()
    print "mac == pc: ", mac == pc # call __cmp__
    print "mac > pc:  ", mac > pc  # call __cmp__
    print "mac < pc:  ", mac < pc  # call __cmp__
    
    newpc = computer('x86', 1024, ['mouse', 'keyboard', 'monitor', 'bluetooth dongle', 'usb flash drive'])
    print newpc[2]
    print newpc[3]
    print newpc[10] == '' # should return blank string
    
    
    # test __setitem__
    newpc[0]='headphones'
    print newpc[0]
    newpc[10]='zip drive'
    print newpc[9], newpc[10]
    
    # test __iter__
    # enumerate simply returns an incremented number for every iteration. it's cleaner than
    # using k=0, k++ for every iteration.
    for i, item in enumerate(newpc):
        print i, item
        
    # test __contains__
    print "cd-rom in pc: ", "cd-rom" in newpc
    newpc[6] = "cd-rom"
    print "just added it... now is cd-rom in newpc: ", "cd-rom" in newpc
    
    # test __call__
    print newpc(50)
    # remember, map calls the function in parameter 1 for each object in parameter 2)
    print map(newpc, (100, 1000, 5555))
    # OK now we're getting funky.
    # for each object in param2 (newpc: so each object is going to be an element of 
    # peripherals, probably because map will call "for obj in param2", meaning it
    # will get a list of the peripherals from __iter__
    # then newpc's __call__ routine will add each number to the string (concatonation)
    # due to the behavior of the __call__ routine.
    print map(newpc, newpc)
        
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
