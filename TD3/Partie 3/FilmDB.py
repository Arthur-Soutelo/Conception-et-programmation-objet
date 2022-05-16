"""
Authors: Arthur SOUTELO ARAUJO
         Valentin CHAZALON
"""
import sqlite3

class FilmDB:
# Initialisation :
    def __init__(self,lib):
        self.__conn = sqlite3.connect(lib)          # Connexion avec la base de données
        self.__curseur = self.__conn.cursor()
        
    def __del__ (self):
        self.__conn.close()                         # Fermer connexion avec la base de données
        
# Fonctions get :
    def get_film(self, idFilm):                     # Selectioner un film à partir d'un ID
        try:
            self.__curseur.execute("SELECT * FROM films WHERE id=('{}')".format(idFilm))
        except sqlite3.OperationalError as err:                                # interception d'une exception
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 
        else:
            return self.__curseur.fetchone()

    def get_realisateur(self, idRealisateur):       # Selectioner un realisateur à partir d'un ID
        try:
            self.__curseur.execute("SELECT * FROM realisateurs WHERE id=('{}')".format(idRealisateur))
        except sqlite3.OperationalError as err:                                # interception d'une exception
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 
        else:
            return self.__curseur.fetchone()

# Fonctions pour chercher de base :
    def chercher_films_acteur(self, nomActeur):     # Creer une liste avec tous les films qui ont comme acteur principal le parametre
        try:
            self.__curseur.execute("SELECT id FROM acteurs WHERE nom='{}'".format(nomActeur))
            self.__id_acteur = self.__curseur.fetchone()
            self.__id_acteur = int(self.__id_acteur[0])
            
            self.__curseur.execute("SELECT * FROM distributions WHERE idacteur='{}'".format(self.__id_acteur))
            self.__liste_id_films = self.__curseur.fetchall()
            
            self.__liste_films = []
            for ligne in self.__liste_id_films:
                self.__film = self.get_film(ligne[0])
                self.__liste_films.append(self.__film)

            self.__liste_films_fin = []
            for ligne in self.__liste_films:
                self.__realisateur = self.get_realisateur(int(ligne[5]))
                self.__new_ligne = [ligne[0],ligne[1],ligne[2],ligne[3],ligne[4],"".join(self.__realisateur[1])]
                self.__liste_films_fin.append(self.__new_ligne)
               
        except sqlite3.OperationalError as err:                                # interception d'une exception
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 
        
        else:
            return self.__liste_films_fin
    
    def chercher_films_realisateur(self, nomRealisateur):       # Creer une liste avec tous les films qui ont comme realisateur le parametre
        try:
            self.__curseur.execute("SELECT id FROM realisateurs WHERE nom='{}'".format(nomRealisateur))
            self.__id_realisateur = self.__curseur.fetchone()
            self.__id_realisateur = int(self.__id_realisateur[0])
            
            self.__curseur.execute("SELECT * FROM films WHERE idrealisateur='{}'".format(self.__id_realisateur))
            self.__liste_films = self.__curseur.fetchall()
    
            self.__liste_films_fin = []
            for ligne in self.__liste_films:
                self.__realisateur = self.get_realisateur(int(ligne[5]))
                self.__new_ligne = [ligne[0],ligne[1],ligne[2],ligne[3],ligne[4],"".join(self.__realisateur[1])]
                self.__liste_films_fin.append(self.__new_ligne)
                
        except sqlite3.OperationalError as err:                                # interception d'une exception
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 
        else:
            return self.__liste_films_fin
    
    def chercher_films_periode(self, debut, fin):               # Creer une liste avec tous les films dans le periode especifique
        try:
            assert debut <= fin, "Debut apres le fin"
            
            self.__curseur.execute("SELECT * FROM films WHERE annee BETWEEN '{}' AND '{}'".format(debut, fin))
            self.__liste_films = self.__curseur.fetchall()
            
            self.__liste_films_fin = []
            for ligne in self.__liste_films:
                self.__realisateur = self.get_realisateur(int(ligne[5]))
                self.__new_ligne = [ligne[0],ligne[1],ligne[2],ligne[3],ligne[4],"".join(self.__realisateur[1])]
                self.__liste_films_fin.append(self.__new_ligne)
            
        except sqlite3.OperationalError as err:                                # interception d'une exception
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            return None 
        except AssertionError as msg:
            print(msg)
            return [] 
        
        else:
            return self.__liste_films_fin

    
# Fonctions pour chercher composées :
    def chercher_films_acteur_periode(self, nomActeur, debut, fin):            # Creer une liste avec tous les films qui ont comme acteur principal le parametre dans le periode especifique
        self.__liste_films_acteur = self.chercher_films_acteur(nomActeur)
        self.__liste_films_periode = self.chercher_films_periode(debut, fin)
        self.__liste = self.common_elements(self.__liste_films_acteur,self.__liste_films_periode)
        return self.__liste
        
        
    def chercher_films_realisateur_periode(self, nomRealisateur, debut, fin):  # Creer une liste avec tous les films qui ont comme realisateur le parametre dans le periode especifique
        self.__liste_films_realisateur = self.chercher_films_realisateur(nomRealisateur)
        self.__liste_films_periode = self.chercher_films_periode(debut, fin)
        self.__liste = self.common_elements(self.__liste_films_realisateur,self.__liste_films_periode)
        return self.__liste
 
# Fonctions EXTRAS :
    def common_elements(self, list1, list2):        # Fait un comparaison entre deux listes e donne une liste avec les ellements qui son commum à les deux
        result = []
        for element in list1:
            if element in list2:
                result.append(element)
        return result

# Tests :
if __name__ == '__main__':
    aFilmDB = FilmDB('films.sqlite3')
    liste_films = aFilmDB.chercher_films_acteur("Harrison Ford")
    print(liste_films)
    
    print("\n\n\n\n\n")
    
    liste_films_res = aFilmDB.chercher_films_realisateur("Ridley Scott")
    print(liste_films_res)

    print("\n\n\n\n\n")
    
    liste_films_periode = aFilmDB.chercher_films_periode(1920, 1924 )
    print(liste_films_periode)

    print("\n\n\n\n\n")
    
    liste_films_periode_acteur = aFilmDB.chercher_films_acteur_periode("Harrison Ford",1980, 1983 )
    print(liste_films_periode_acteur)

    print("\n\n\n\n\n")
    
    liste_films_periode_realisateur = aFilmDB.chercher_films_realisateur_periode("Ridley Scott",1980, 1983 )
    print(liste_films_periode_realisateur)

    aFilmDB.__del__()
    
    