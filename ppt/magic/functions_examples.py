'''
    Working with functions
'''

# one parameter, required
def person1(name):
    print "My name is %s" % name
    
#one parameter, optional w/ default argument
def person2(name='ken'):
    print "My name is %s" % name
    
#three parameters, two optional
def person3(name, city='cincinnati', work='library'):
    print "My name is %s from %s, I work at %s" % (name, city, work)
    
#one required parameter, the rest are variable
def person4(name, *params):
    print "My name is %s, my parameter list is:" % name
    for i in params:
        print i
        
#one required param, variable keywords
def person5(name, **keywords):
    print "My name is %s" % name
    if keywords.has_key('city'):
        print "I am from %s" % keywords['city']
    for kw,val in keywords.items():
        print "%s: %s" % (str(kw), str(val))
        
# one required param, then variable params, then variable keywords
def person6(*params, **keywords):
    if keywords.has_key('name'):
        name = keywords['name']
    else:
        name = 'anonymous'
    print "My name is %s" % name
    print "My params are:"
    for i, p in enumerate(params):
        print "%d. %s" % (i, str(p))
    print "My keywords are:"
    # Note the use of a tuple unpacking from enumerate...
    for i, (key, val) in enumerate(keywords.items()):
        print "%d. %s:%s" % (i, str(key), str(val))
        
    print "Now I'm going to call the function contained in the keyword 'func':"
    if keywords.has_key('func'):
        print "==== result from calling: %s =====" % keywords['func']
        keywords['func'](**keywords)
    else:
        print "no function found"
        
# simple usage
print 'person1'
person1('blaine')
print ''
print 'person2'
person2()
person2('ken')
print ''
print 'person3'
person3('blaine')
person3('blaine', 'dayton', 'airport')
person3('blaine', work='coffee shop')
person3('blaine', work='donut shop', city='san francisco')
print ''
print 'person4'
person4('blaine', 'random', 'parameters', 'for', 5, 19, person4)
# * means "take everything in range(10) and make them actual arguments. don't pass in a list of numbers,
# pass in parameters of integers
person4('blaine', *range(10)) 
# but you could do this too!
person4('blaine', range(10))
print ''
print 'person5'
person5('blaine', keyword='mykeyword', city='columbus, ohio')
person5(city='cleveland', name='blaine')
print ''
print 'person6'
person6(1,2,3,4,5, name='blaine', city='cincinnati', work='clifton labs')

# pay attention now, this gets interesting!
person6(1,2,3,4, name='blaine', city='cincinnati', work='cliftonlabs', func=person5)

