
class Audition:
   all =[]
   def __init__(self, actor, location, role, hired = False):
      self.actor = actor
      self.location = location
      self.role = role
      self.hired = False
      Audition.all.append(self)
      #return [r for r in self.auditions]

   #call_back()` will change the the
   # hired attribute to `True`.
   def call_back(self): 
      self.hired == False 


         # hired_attribute = self.actor for a in actor.auditions if call_back == hired_attribute
         # if call_back is self.actor 
         #    return True
         # else: 
         #    false        