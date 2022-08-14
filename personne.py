class Personne:
    def __init__(self, name, last_name, eyes, hair, account):
       self.name = name
       self.last_name = last_name
       self.eyes = eyes
       self.hair = hair
       self.account = account

class Worker(Personne):
    def __init__(self, name, last_name, eyes, hair, account):
        super().__init__(name, last_name, eyes, hair, account)
    
    def working(self):
        pass    
        
class Employee(Personne):
    def __init__(self, name, last_name, eyes, hair, account):
        super().__init__(name, last_name, eyes, hair, account)
    
    def working(self):
        pass

class Criminal(Personne):
    def __init__(self, name, last_name, eyes, hair, account):
        super().__init__(name, last_name, eyes, hair, account)
    
    def steal(self):
        pass #le criminel peut choisir quand il veut partir
    
class Cops(Personne):
    def __init__(self, name, last_name, eyes, hair, account):
        super().__init__(name, last_name, eyes, hair, account)
    
    def arrival(self):
        pass #ici je voudrais un timer de 30 seconde avant de lancer l'arrestation n\
            #du criminel, par contre si la police arrive avant il ne pourra pas s'échapper et sera arrêté 
        