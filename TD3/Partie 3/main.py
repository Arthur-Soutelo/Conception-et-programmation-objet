"""
Authors: Arthur SOUTELO ARAUJO
         Valentin CHAZALON
"""

from FilmDB import FilmDB
import matplotlib.pyplot as plt
import numpy             as np

# Plot graphique de barre de la quantite de films dans un periode:
def plot_bar_quantite_films(vect,debut, fin):
    try:
        assert debut <= fin, "Debut apres le fin"
        x = np.arange(abs(fin-debut+1))
        x = x + debut           # Vecteur de Temps
            
        y = np.zeros(abs(fin-debut+1))
        for i in x:
            for film in vect:
                if i == int(film[2]):
                    y[i-debut] = y[i-debut] + 1
            
        width = 0.5
        plt.bar(x,y,width,color='b')
        
        plt.ylabel('Nombre de films')
        plt.xlabel('Année de sortie')
        
        plt.title('Films en fonction des années')
        plt.show()
    except AssertionError as msg:
        print(msg)
        return None

# Plot graphique de camembert selon les notes des films dans un periode:
def plot_pie_score_periode(vect, debut, fin):
    try:
        assert debut <= fin, "Debut apres le fin"
        notes = []
        for film in vect:
            if float(film[3]) not in notes:
                notes.append(float(film[3]))
        notes.sort()
        
        quantite = np.zeros(len(notes))
        
        i=0
        for note in notes:
           for film in vect:
               if film[3] == note:
                   quantite[i] = quantite[i] + 1
           i = i + 1
        
        plt.pie(quantite, labels=notes,shadow=True, startangle=90)
        #plt.pie(quantite, labels=notes, autopct='%1.1f%%',shadow=True, startangle=90)
        plt.axis('equal')
        
        plt.title('Notes dans le periode ' + str(debut) + ' - ' + str(fin))
        plt.show()
    except AssertionError as msg:
        print(msg)
        return None

# Plot graphique de barre de la quantite de films dans un periode: (mais a comme argument tout la librairie)
def plot_bar(lib,debut, fin):
    try:
        assert debut <= fin, "Debut apres le fin"
        x = np.arange(abs(fin-debut+1))
        x = x + debut           # Vecteur de Temps
            
        y = np.zeros(abs(fin-debut+1))
        for i in x:
            y[i-debut] = len(lib.chercher_films_periode(i,i))
            
        width = 0.5
        plt.bar(x,y,width,color='b')
        
        plt.ylabel('Nombre de films')
        plt.xlabel('Année de sortie')
        
        plt.title('Films en fonction des années')
        plt.show()
    except AssertionError as msg:
        print(msg)
        return None

if __name__ == '__main__':
    aFilmDB = FilmDB('films.sqlite3')
    
    
    debut = 1940
    fin = 2000
    acteur = "Harrison Ford"
    realisateur = 'Alfred Hitchcock'
    
    vector_all = aFilmDB.chercher_films_periode(debut, fin)
    vector_acteur = aFilmDB.chercher_films_acteur_periode(acteur, debut, fin)
    vector_realisateur = aFilmDB.chercher_films_realisateur_periode(realisateur, debut, fin)
    
    # Plots:
    plot_bar(aFilmDB, debut, fin)
    
    plot_pie_score_periode(vector_all, debut, fin)
    plot_bar_quantite_films(vector_all,debut, fin)
    
    plot_pie_score_periode(vector_acteur, debut, fin)
    plot_bar_quantite_films(vector_acteur,debut, fin)
    
    plot_pie_score_periode(vector_realisateur, debut, fin)
    plot_bar_quantite_films(vector_realisateur,debut, fin)

    # Plots exceptions:
    debut = 3000
    fin = 1000
    
    plot_bar(aFilmDB, debut, fin)
    
    plot_pie_score_periode(vector_all, debut, fin)
    plot_bar_quantite_films(vector_all,debut, fin)
    
    plot_pie_score_periode(vector_acteur, debut, fin)
    plot_bar_quantite_films(vector_acteur,debut, fin)
    
    plot_pie_score_periode(vector_realisateur, debut, fin)
    plot_bar_quantite_films(vector_realisateur,debut, fin)

    aFilmDB.__del__()