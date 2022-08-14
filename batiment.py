from personne import Cops

class Building:
    def __init__(self, adress, floors):
        self.adress = adress
        self.floors = floors
    
    def get_adress(self):
        return self.adress
    
    def get_floors(self):
        return self.floors

class Banque(Building):
    def __init__(self, adress, floors, name, BIC, representative):
        super().__init__(adress, floors)
        self.name = name
        self.BIC = BIC
        self.representative = representative
        print("La banque", name, "situé à", adress, "possède", floors, " étages . Son BIC est",BIC, " et son représentant est", representative)
    
    def call_the_cops(self):
        Cops.arrival()            
              
class Maison(Building):
    def __init__(self, adress, floors, family_name, occupant):
        super().__init__(adress, floors)
        self.family_name = family_name
        self.occupant = occupant
        print(f"La maison situé à {adress} possède {floors} étages et appartient à la famille {family_name}, et possède {occupant} comme occupants")

class Commerce(Building):
    def __init__(self, adress, floors, categories, holder):
        super().__init__(self, adress, floors)
        self.catgories = categories #type of product
        self.holder = holder #name of the building holder
        print(f"le commerce situé à {adress} possède {floors} et vend des marchandises de type {categories} et appartient à {holder}")        