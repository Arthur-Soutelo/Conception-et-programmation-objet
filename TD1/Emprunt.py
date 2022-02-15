from datetime import date

from Livre import livre
from Lecteur import lecteur

class emprunt:
    def __init__(self,num_lecteur,num_livre):
        self.__lecteur = num_lecteur
        self.__livre = num_livre
        self.__date = date.isoformat(date.today())
        
    def __str__(self):
        print('Lecteur : ' + str(self.__lecteur))
        print('Livre : ' + str(self.__livre))
        print('Date : ' + str(self.__date))
    
    def get_numero_lecteur(self):
        return self.__lecteur
    
    def get_numero_livre(self):
        return self.__livre
    
    def get_date(self):
        return self.__date
    

    
    
if __name__ == '__main__':
    E1 = emprunt(1, 101)
    print(E1)
    