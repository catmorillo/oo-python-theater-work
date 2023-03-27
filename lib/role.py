from .audition import Audition


class Role:
    def __init__(self, character_name):
        self.character_name = character_name
    
#auditions returns all of the auditions associated
# with this role.
    @property
    def auditions(self): 
        return [a for a in Audition.all if a.role == self] 

#actors` returns a list of names from the actors associated 
#with this role.  
    @property 
    def actors(self):
        return [a.actor for a in self.auditions] 
#returns a list of locations from the auditions associated
#with this role.
    @property 
    def locations(self):
        return [a.location for a in self.auditions]

#lead` returns the first instance of the audition that 
#was hired for this role or returns a string 'no actor has
#been hired for this role

    @property 
    def lead(self):
        for audition in self.auditions:
            if audition.hired:
                return audition 
        return: "no actor has been hired for this role"



##understudy` returns the second instance of the audition 
#that was hired for this role or returns a string 'no actor 
#has been hired for understudy for this role'.

    # @property
    # def understudy(self):
    #     hired_actors = [a for a in self.audition if audition.hired ]
    

