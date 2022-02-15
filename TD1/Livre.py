class livre:
    def __init__(self,a,t,n,ne):
        self.__auteur = a
        self.__titre = t
        self.__numero = n
        self.__n_exemplaires = ne
    
    def __str__(self):
        S = 'Auteur : ' + str(self.__auteur) + '\n'
        S += 'Titre : ' + str(self.__titre) + '\n'
        S += 'Numero : ' + str(self.__numero) + '\n'
        S += 'Nombre d\'exemplaires : ' + str(self.__n_exemplaires) + '\n'
        return S
    
    def get_auteur(self):
        return self.__auteur
    def get_titre(self):
        return self.__titre
    def get_numero(self):
        return self.__titre
    def get_exemplaires(self):
        return self.__n_exemplaires
    
    def set_exemplaires(self, newn):
        self.__n_exemplaires = newn
        
if __name__ == '__main__':
    B1 = livre('Albert Camus', 'L\'etranger', 101, 2)
    B2 = livre('Antoine de Saint-Exupery','Le petit prince', 102,2)
    B3 = livre('Amin Maalouf', 'Léon l\'Africain', 103, 2)
    
    print('Livre 101 : \n', B1)
    print('Livre 102 : \n', B2)
    print('Livre 103 : \n', B3)

