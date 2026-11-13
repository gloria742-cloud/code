#classe Personne
class personne:
    def __init__(self, prenom,nom,age):
        self.prenom=prenom
        self._nom=nom
        self.__age=age

#code principal
alice = personne("alice", "dupont", 20)
print(alice.prenom)
print(alice._nom)
print(alice.__age)
