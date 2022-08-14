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
        pass