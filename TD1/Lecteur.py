class lecteur:
    def __init__(self,nom,a,n):
        self.__nom = nom
        self.__adresse = a
        self.__numero = n
        self.__nb_emprunts = 0
    
    def __str__(self):
        S = 'Nom Complet : ' + str(self.__nom) + '\n'
        S += 'Adresse : ' + str(self.__adresse) + '\n'
        S += 'Numero : ' + str(self.__numero) + '\n'
        return S
    
    def get_nom(self):
        return self.__nom
    def get_adresse(self):
        return self.__adresse
    def get_numero(self):
        return self.__numero
    def get_nb_emprunt(self):
        return self.__nb_emprunts
    
    def increment_nb_emprunts(self):
        self.__nb_emprunts += 1
    def decrement_nb_emprunts(self):
        self.__nb_emprunts += -1
    
    
if __name__ == '__main__':
    L1 = lecteur('Giovanni', '51 Chemin des Mouilles', 1)
    L2 = lecteur('Eduardo Guedes', 'Rue de la Gare', 2)
    L3 = lecteur('Dimitri', 'Impasse de La Fayette', 3)
    L4 = lecteur('Rodriguez Alfonso', 'Rue du Stade', 4)

    print('Lecteur 1 : \n', L1)
    print('Lecteur 2 : \n', L2)
    print('Lecteur 3 : \n', L3)
    print('Lecteur 4 : \n', L4)
