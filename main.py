
from batiment import Banque, Commerce, Maison
from personne import Worker, Employee, Criminal

BNP = Banque("rue de la radinerie", 8,"BNP","GEBABEBB", "Gilbert Montagnier")
#residential_house = Maison("rue de la maison", 2, "Sanders", ["Erwann Sanders", "Théa Sanders", "Elea Sanders", "Robert Sanders"])
#commerce = Commerce("rue du commerce", 3, "alimentaire", "Jean Dujardin")
BNP.call_the_cops()
