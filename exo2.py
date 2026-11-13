#classe personne
class personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    def se_presenter(self):
        print(f"bonjour, je suis{self.nom}et j'ai{self.age}ans.")

alice= personne("Alice",20)
alice.se_presenter()