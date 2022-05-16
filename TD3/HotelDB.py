import sqlite3

class HotelDB:
    def __init__(self,lib):
        self.__conn = sqlite3.connect(lib)
        self.__curseur = self.__conn.cursor()
        
    def get_name_hotel_etoile(self, nbEtoiles):
        try:
           self.__curseur.execute("SELECT nom FROM hotel WHERE etoiles=:x;", {"x":nbEtoiles})
           return self.__curseur.fetchall()
               
        except sqlite3.OperationalError as err:                                # interception d'une exception quelconque
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 

    def nouveau_client(self, nom, prenom):
        self.__flag = 0
        try:
           for ligne in self.__curseur.execute("SELECT * FROM client"):
               if ligne[1] == nom and ligne[2] == prenom:
                   self.__flag = 1
                   return ligne[0]
               else:
                   pass
               
           if self.__flag == 0:
               self.__curseur.execute("INSERT INTO client(nom, prenom) VALUES ('{}','{}')".format(nom, prenom))
               self.__conn.commit()
               print ("Client ajouté")
           else:
               print("Client deja existant")
               
           return self.__curseur.fetchall()
               
        except sqlite3.OperationalError as err:                                # interception d'une exception quelconque
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 

    def __del__ (self):
        self.__conn.close() 
    


if __name__ == '__main__':
    try:
        aHotelDB = HotelDB('hotellerie.db')
        nbEtoiles = 2
        resultat = aHotelDB.get_name_hotel_etoile(nbEtoiles)
        print("Liste des noms d'hotel", nbEtoiles, "étoiles : ", resultat)
        
        numclient = aHotelDB.nouveau_client("Dupont", "Marcelo")
        print(numclient)

    except Exception as err:                                # interception d'une exception quelconque
        print('err:', str(err))
        print('type exception:', type(err).__name__)
    finally:                                                # fermeture de la base dans tous les cas
        aHotelDB.__del__()


