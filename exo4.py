class etudiant:
    def __init__(self,prenom,nom,age,niveau):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.niveau = niveau
    def se_presenter(self):
        print(f"bonjour, je suis{self.prenom, self.nom} j'ai{self.age} ans et je suis etudiante {self.niveau}")

       #corps principal
alice=etudiant("alice","smith",20,"Master1")


alice.se_presenter()