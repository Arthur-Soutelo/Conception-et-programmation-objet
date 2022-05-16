"""
Authors: Arthur SOUTELO ARAUJO
         Valentin CHAZALON
"""
import sqlite3

class JoueurDB:
    def __init__(self,lib):
        self.__conn = sqlite3.connect(lib)
        self.__curseur = self.__conn.cursor()
    
    def __del__ (self):
        self.__conn.close() 
        
    def existenceTables(self):
        self.__curseur.execute("SELECT name FROM sqlite_master WHERE type='table' ")
        if bool(self.__curseur.fetchone()) is False:
            self.createTables()
        
    def createTables(self):
        self.__curseur.execute("CREATE TABLE Joueur (idjoueur INTEGER PRIMARY KEY AUTOINCREMENT, pseudo VARCHAR(255))")
        self.__curseur.execute("CREATE TABLE Partie (idpartie INTEGER PRIMARY KEY AUTOINCREMENT, idjoueur INTEGER, mot VARCHAR(255), score FLOAT)")    
        self.__conn.commit()
        
    def nouveau_joueur(self, pseudo):
        self.existenceTables()
        try:
            self.__curseur.execute("SELECT * FROM Joueur WHERE pseudo = '{}'".format(pseudo))
            if len(self.__curseur.fetchall()) != 0:
                print("Pseudo deja existant")
            else:
                self.__curseur.execute("INSERT INTO Joueur(pseudo) VALUES ('{}')".format(pseudo))
                self.__conn.commit()
                print ("Joueur ajouté")
               
        except sqlite3.OperationalError as err:                                # interception d'une exception quelconque
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            
    
    def nouvelle_partie(self, idjoueur, mot, score):
        self.existenceTables()
        try:
            self.__curseur.execute("INSERT INTO Partie(idjoueur, mot, score) VALUES ('{}','{}','{}')".format(idjoueur, mot, score))
            self.__conn.commit()
            print ("Partie enregistrée")
               
        except sqlite3.OperationalError as err:                                # interception d'une exception quelconque
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            
    def getIDJoueur(self, pseudo):
        self.existenceTables()
        self.__curseur.execute("SELECT idjoueur FROM Joueur WHERE pseudo = '{}'".format(pseudo))
        indice = self.__curseur.fetchone()
        if indice == None:
            self.nouveau_joueur(pseudo)
            self.__curseur.execute("SELECT idjoueur FROM Joueur WHERE pseudo = '{}'".format(pseudo))
            indice = self.__curseur.fetchone()
            
        idJoueur = list(str(indice))
        idJoueur.pop()
        idJoueur.pop()
        idJoueur.pop(0)
        idJoueur = "".join(idJoueur)
        return int(idJoueur)
        
    def getJoueurs(self):
        self.existenceTables()
        try:
           self.__curseur.execute("SELECT * FROM Joueur")
           return self.__curseur.fetchall()
        except sqlite3.OperationalError as err:                                # interception d'une exception quelconque
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 

    def getParties(self):
        self.existenceTables()
        try:
           self.__curseur.execute("SELECT * FROM Partie")
           return self.__curseur.fetchall()
        except sqlite3.OperationalError as err:                                # interception d'une exception quelconque
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 


if __name__ == '__main__':
    try:
        test = JoueurDB('pendu.db')
    except Exception as err:                                # interception d'une exception quelconque
        print('err:', str(err))
        print('type exception:', type(err).__name__)    
    finally:                                                # fermeture de la base dans tous les cas
        
        # test.nouveau_joueur('Victor')
        # print(test.getIDJoueur('Arthur'))
        # test.nouvelle_partie(1, 'mot', 58)
        
        print(test.getIDJoueur("dasda"))
        
        print(test.getParties())
        
        test.__del__()