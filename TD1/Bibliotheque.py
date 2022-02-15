from Livre import livre
from Lecteur import lecteur
from Emprunt import emprunt

class bibliotheque:
    def __init__(self,nom):
        self.__nom = nom
        self.__lecteurs = []
        self.__livres = []
        self.__emprunts = []
        
    def __str__(self):
        print('Nom : ' + str(self.__nom))
        
# Lecteur:
    def ajout_lecteur(self, unLecteur):
        self.__lecteurs.append(lecteur(unLecteur))
        
    def affiche_lecteurs(self):
        for i in self.lecteurs:
            print(i)
 
    def chercher_lecteur_numero(self,numero):
        for i in self.__lecteurs:
            if i.get_numero() == numero:
                return i
            return None
        
    def chercher_lecteur_nom(self,nom):
       for i in self.__lecteurs:
           if i.get_nom() == nom:
               return i
           return None
        
# Livre:    
    def ajout_livre(self, unLivre):
        self.__livres.append(livre(unLivre))

    def affiche_livres(self):
        for i in self.livres:
            print(i)
    
    def chercher_livre_numero(self, numero):
        for i in self.livres:
            if i.get_numero() == numero:
                return i
            return None
        
    def chercher_livre_titre(self, titre):
        for i in self.livres:
            if i.get_titre() == titre:
                return i
            return None
            
 # Emprunt:
    def emprunt_livre(self, num_lecteur, num_livre)
        livre = self.chercher_livre_numero()
        if livre == None:
            
        
    def retour_livre(self,num_lecteur, num_livre):
        lecteur.decrement_nb_emprunts()
        
        
    
if __name__ == '__main__':
    C1 = bibliotheque('Michel Serre')
    print(C1)
    
    C1.ajout_lecteurs('Giovanni', '51 Chemin des Mouilles',2)