class comptebancaire :
    def __init__(self,nom,solde):
        self.nom = nom
        self.solde = solde
    def deposer  (self, montant):
        self.solde += montant

        def retirer  (self, montant):
            if montant <= self.solde :
              self.solde += montant
            else:
             print("solde insuffisant")
        
        def Affichersolde (self):
            print(f" votre solde est de{self.solde} $")
