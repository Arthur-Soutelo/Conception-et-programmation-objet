"""
Authors: Arthur SOUTELO ARAUJO
         Valentin CHAZALON
"""
from FilmDB import FilmDB

def choix_utilisateur():
    liste_films = []
    print("Bienvenue au service de streaming ECLflix! \n"
          "Vous voulez chercher: \n")
    val = int(input(" [1] Films par Acteur \n"
                    " [2] Films par Realisateur \n"))
    if val == '1':                                  # [1] Films par Acteur
        nomActeur = str(input("Nom du Acteur : "))
        print("Voulez vous chercher dans un periode especifique ?")
        bol = int(input(" [0] Non \n"
                        " [1] Oui \n"))
        if bol == 0:
            liste_films = FilmDB.chercher_films_acteur(nomActeur)
        elif bol == 1:
            debut = input("Debut : ")
            fin = input("Fin : ")
            liste_films = FilmDB.chercher_films_acteur_periode(nomActeur, debut, fin)
        else:
            print ("Valeur non valide. \nVeuillez reessayer")
        
    elif val == '2':                                # [2] Films par Realisateur
        nomRealisateur = input("Nom du Realisateur : ")
        print("Voulez vous chercher dans un periode especifique ?")
        bol = input(" [0] Non \n"
                    " [1] Oui \n")
        if bol == '0':
            liste_films = FilmDB.chercher_films_realisateur(nomRealisateur)
        elif bol == '1':
            debut = input("Debut : ")
            fin = input("Fin : ")
            liste_films = FilmDB.chercher_films_realisateur_periode(nomRealisateur, debut, fin)
        else:
            print ("Valeur non valide. \nVeuillez reessayer")
        
    else:                                           # Valeur non valide
        print ("Valeur non valide \n\nVeuillez reessayer")
        
    return liste_films


if __name__ == '__main__':
