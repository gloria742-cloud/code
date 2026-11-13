class personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    def anniversaire(self):
        self.age += 1
       
#code principal
alice= personne("Alice",20)
print(alice.age)
alice.anniversaire()
print(alice.age)
