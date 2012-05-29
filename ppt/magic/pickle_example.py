from magic_methods import computer
import cPickle as pickle # good to keep pickle as the name for less confusion and compatibility

# make a simple object
obj = {'name': 'blaine',
       'city': 'cincinnati',
       'favorite food': 'pizza'}
       
# save it for later
pickle.dump(obj, open("blaine.pickle", "w"))

# then we can load it up at a later time quickly
loaded = pickle.load(open("blaine.pickle")) # open() is 'read' by default

# we can do this with classes, too, but we have to be careful that the
# class is available in the namespace that we load into. In other words,
# pickle will dump the instance but not the definition of the class.

comp = computer("Gameboy", 16, ['buttons', 'screen', 'speakers', 'battery', 'plastic case'])
print comp

# save it for later
print 'saving to computer.pickle'
pickle.dump(comp, open("computer.pickle", "w"))

# delete it
print 'deleting computer instance'
del comp

# load it back up!
comp = pickle.load(open("computer.pickle"))
print comp
