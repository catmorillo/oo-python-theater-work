import ipdb
from lib import *

# Test your code below...
r1 =Role("Wonderwoman")
r2 =Role("Batman")
r3 =Role("Spiderman")
r4 =Role("Catwoman")

a1 = Audition("Gal Gadot", "Los Angeles", True, r1)
a2 = Audition("Christian Bale", "New York", False, r2)
a3 = Audition("Tom Holland", "New York", True, r3)
a4 = Audition("Halle Berry", "New York", True, r4)

# the below line allows us to stop & try stuff!
ipdb.set_trace()

