"""
Authors: Arthur SOUTELO ARAUJO
         Valentin CHAZALON
"""

from tkinter import * 
from formes import Forme 
from formes  import Rectangle 
from formes import Ellipse 
from random import randint
from tkinter import colorchooser
from tkinter import messagebox
from  tkinter import ttk


from JoueurDB import JoueurDB

class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)        
        
        # Variables
        self.chargeMots()           # Creates a vector with the words form the file
        self.__error = 0
        self.text = StringVar()
        self.__couleurBG = "black"
        self.__vectChoix=[]
        self.__pseudo = ""
        self.__decision = "no"
        
        # paramètres de la fenêtre
        self.configure(bg=self.__couleurBG)
        self.title('Jeu du pendu')
        self.geometry('500x700+400+400')
        
        # Pose la question de login
        self.Question()
        
        # Frames
        self.__Frame1 = Frame(self, width=300, height=50, bg=self.__couleurBG)
        Frame2 = Frame(self, width=350, height=350)
        self.__mot_label = Label(self, textvariable=self.text, fg='white', bg=self.__couleurBG, font=("Helvetica", 14))
        self.__Frame4 = Frame(self, width=400, height=250, bg=self.__couleurBG)    
        self.__Frame5 = Frame(self, width=300, height=50, bg=self.__couleurBG)
        # Frames PACK
        self.__Frame1.pack(side=TOP, padx=0, pady=10)
        Frame2.pack(side=TOP, padx=10, pady=10)
        self.__mot_label.pack(side=TOP, padx=5, pady=5)
        self.__Frame4.pack(side=TOP, padx=5, pady=5)
        self.__Frame5.pack(side=TOP, padx=0, pady=10)
        
        # Menu
        self.__menubar = Menu(self)
        
        self.__menu2 = Menu(self.__menubar, tearoff=0)
        self.__menubar.add_cascade(label="Enregistrement désactivé", menu=self.__menu2)    
        self.__menu2.add_command(label="Déconnexion/Connexion", command=self.DeconnexionConnexion)
        
        self.__menu1 = Menu(self.__menubar, tearoff=0)
        self.__menu1.add_command(label="Couleur Fond", command=self.selection_couleur_bg)
        self.__menu1.add_separator()
        self.__menu1.add_command(label="Couleur Boutons", command=self.selection_couleur_bouton)
        self.__menu1.add_command(label="Couleur Clavier", command=self.selection_couleur_clavier)
        self.__menu1.add_separator()
        self.__menu1.add_command(label="Couleur Canvas", command=self.selection_couleur_canvas)
        self.__menu1.add_separator()
        self.__menu1.add_command(label="Couleur Personnage", command=self.selection_couleur_personnage)
        self.__menu1.add_command(label="Couleur Potence", command=self.selection_couleur_potence)
        self.__menubar.add_cascade(label="Changer Couleur", menu=self.__menu1)
    
        self.__menu3 = Menu(self.__menubar, tearoff=0)
        self.__menubar.add_cascade(label="Affichage", menu=self.__menu3)    
        self.__menu3.add_command(label="Joueurs", command=self.Affiche_Joueurs)
        self.__menu3.add_command(label="Parties", command=self.Affiche_Parties)
        
        self.config(menu=self.__menubar)
        
        # Boutons 
        self.__BoutonNouvellePartie=Button(self.__Frame1, text='Nouvelle partie',height= 2, width=15)
        self.__BoutonQuitter=Button(self.__Frame1, text='Quitter',height= 2, width=15)
        self.__BoutonUndo=Button(self.__Frame5, text='Undo',height= 2, width=10)
        # Boutons PACK
        self.__BoutonNouvellePartie.pack(side=LEFT, padx=10, pady=5)
        self.__BoutonQuitter.pack(side=LEFT, padx=5, pady=5)
        self.__BoutonUndo.pack(side=TOP, padx=5, pady=5)
        # Boutons CONFIG
        self.__BoutonQuitter.config(command=self.quit,  borderwidth=3)
        self.__BoutonNouvellePartie.config(command=self.nouvelle_partie,  borderwidth=3)  
        self.__BoutonUndo.config(command=self.triche, borderwidth=3)
        # Clavier
        self.clavier(self.__Frame4)        
        
        # Canvas
        self.__canvas = ZoneAffichage(Frame2,300,300,'white')
        self.__canvas.pack(padx=5,pady=5)
    
    # Méthodes
    def clavier(self,Frame):        # Creates all keyboard buttons (From A to Z)
        self.Boutonslettres= []
        for i in range(26):
            self.Boutonslettres.append(MonBoutonLettre(Frame,self,i, 8))
            if i<=6:
                self.Boutonslettres[i].grid(row=1, column=i)
            if i>6 and i<=13:
                self.Boutonslettres[i].grid(row=2, column=i-7)
            if i>13 and i<=20:
                self.Boutonslettres[i].grid(row=3, column=i-14)
            if i>20:
                self.Boutonslettres[i].grid(row=4, column= i-20)
    
    def chargeMots(self):            # Creates a vector with the words form the file
        f=open('mots.txt', 'r')
        s=f.read()
        self.__mots = s.split('\n')
        f.close()
    
    def nouvelle_partie(self):
        self.__vectChoix=[]
        self.__error = 0
        for i in range(26):             # Resets all keyboard buttons
            self.Boutonslettres[i].config(state=NORMAL)
        self.__BoutonUndo.config(state=NORMAL)
            
        self.__mot = self.__mots[randint(1,len(self.__mots))]   # Chose a random word from the list
        self.__motAffiche = len(self.__mot)*'*'
        self.text.set('Mot : '+str(self.__motAffiche))
        print(self.__mot)
        
        self.__canvas.setStateAllFormes('hidden')
    
    def bonne_lettre(self, lettre):         # Verify if the chosen letter is in the word
        self.__indices=[]
        self.__vectChoix.append(lettre)
        
        for i in range(len(self.__mot)):
            if self.__mot[i] == lettre:
                self.__indices.append(i)
        if len(self.__indices) == 0:
            self.__canvas.showForme(self.__error)
            self.__error = self.__error + 1
            
        return self.__indices
                
        
    def traitement(self, lettre):               # Display correct letters
        self.__indice=[]
        self.__indice = self.bonne_lettre(lettre)
        
        # Substituer les letres
        self.__motListe = list(self.__motAffiche)
        for j in range(len(self.__indice)):
            self.__motListe[self.__indice[j]] = self.__mot[self.__indice[j]]
        self.__motAffiche = "".join(self.__motListe)
        self.text.set('Mot : '+str(self.__motAffiche))
        
        # Verifier la victoire
        self.win_flag = 1
        for i in self.__motAffiche:
            if i == '*':
                self.win_flag = 0
        if self.win_flag == 1:
            self.fin_partie()
        
        # Verifier si la partie est perdue
        if self.__error >= 10:
            self.partie_perdue()
        
    def fin_partie(self):
        self.text.set('Partie gagnée!!!')
        for i in range(26):
            self.Boutonslettres[i].config(state=DISABLED)
        self.__BoutonUndo.config(state=DISABLED)
        if self.__decision == 'yes':
            self.enregistrer_partie()    
        
    def partie_perdue(self):
        self.text.set('Partie perdue')
        for i in range(26):
            self.Boutonslettres[i].config(state=DISABLED)
        self.__BoutonUndo.config(state=DISABLED)
        if self.__decision == 'yes':
            self.enregistrer_partie()

    "  FONCTIONS AUTONOMIE COULEURS  "
    # Couleurs (Exercice 7)
    def selection_couleur_bg(self):
        self.colour = colorchooser.askcolor()
        self.__couleurBG = self.colour[1]
        self.configure(bg=self.__couleurBG)
        self.__Frame1.configure(bg=self.__couleurBG)
        self.__mot_label.configure(bg=self.__couleurBG)
        self.__Frame4.configure(bg=self.__couleurBG)
    def selection_couleur_bouton(self):
        self.colour = colorchooser.askcolor()
        self.__BoutonNouvellePartie.configure(bg=self.colour[1])
        self.__BoutonQuitter.configure(bg=self.colour[1])
    def selection_couleur_clavier(self):
        self.colour = colorchooser.askcolor()
        for i in self.Boutonslettres:
            i.configure(bg=self.colour[1])
    def selection_couleur_canvas(self):
        self.colour = colorchooser.askcolor()
        self.__canvas.configure(bg=self.colour[1])
    def selection_couleur_personnage(self):
        self.colour = colorchooser.askcolor()
        self.__canvas.change_couleur_personnage(self.colour[1])
    def selection_couleur_potence(self):
        self.colour = colorchooser.askcolor()
        self.__canvas.change_couleur_potence(self.colour[1])
        
        "  FONCTION AUTONOMIE TRICHE  "
    def triche(self):
        if len(self.__vectChoix) != 0:
            try:
                let = self.__vectChoix.pop()
            except:
                let = 0
                    
            if let != 0:
                self.__indices=[]
                for i in range(len(self.__mot)):
                    if self.__mot[i] == let:
                        self.__indices.append(i)
                
                if len(self.__indices) != 0:
                    # Substituer les letres
                    self.__motListe = list(self.__motAffiche)
                    for j in range(len(self.__indices)):
                        self.__motListe[self.__indices[j]] = '*'
                    self.__motAffiche = "".join(self.__motListe)
                    self.text.set('Mot : '+str(self.__motAffiche))
                
                elif len(self.__indices) == 0:
                    print(self.__error)
                    self.__canvas.hideForme(self.__error-1)
                    self.__error = self.__error - 1
                    print(self.__error)
                
            for i in self.Boutonslettres:
                if i.getLettre() == let:
                    i.config(state=NORMAL)
                    
        "  FONCTIONS AUTONOMIE BASE DE DONNÉES  "
    def calculate_score(self):
        try:
            score = len(self.__mot)/self.__error
        except ZeroDivisionError as err:
            print('err:', str(err))
            print('type exception:', type(err).__name__)
            score = 1
        return float("{:.2f}".format(score))
    
    def enregistrer_partie(self):
        data = JoueurDB('pendu.db')
        data.nouvelle_partie(data.getIDJoueur(self.__pseudo), self.__mot, self.calculate_score())
        del data
    
    def Question(self):
        self.__decision = messagebox.askquestion("Question", "Voulez vous enregistrer vos resultats?")
        if self.__decision == 'yes':
            self.Login()
    
    def Login(self):
        self._newWindow = Toplevel(self)
        self._newWindow.title("Login")
        self._newWindow.geometry("300x100")
        
        lab = Label(self._newWindow, text="Votre Pseudo : ")
        self._ent = Entry(self._newWindow, bd =5)
        self._but = Button(self._newWindow, text='OK',height= 2, width=5)
        
        lab.pack( side = LEFT)
        self._ent.pack(side = LEFT)
        self._but.pack(side = LEFT)
        
        self._but.config(command=self.PseudoOK)
        
    def PseudoOK(self):
        self.__pseudo = self._ent.get()
        self._but.config(state=DISABLED)
        self._newWindow.destroy()
        self.__menubar.entryconfigure(1, label="User : " + str(self.__pseudo))
        print(self.__pseudo)
    
    def DeconnexionConnexion(self):
        if self.__decision == "yes":
            self.__menubar.entryconfigure(1, label="Enregistrement désactivé")
            self.__decision = "no"
        elif self.__decision == "no":
            self.__decision = "yes"
            self.Login()
            self.__menubar.entryconfigure(1, label="User : " + str(self.__pseudo))    
            
    def Affiche_Joueurs(self):
        data = JoueurDB('pendu.db')
        self.__Joueurs = data.getJoueurs()
        del data
        
        self._newWindow2 = Toplevel(self)
        self._newWindow2.title("Liste Joueurs")
        self._newWindow2.geometry("200x250")        
        table = ttk.Treeview(self._newWindow2)
        table.pack()
        table['columns'] = ('idjoueur', 'pseudo')
        table.column("#0", width=0,  stretch=NO)
        table.column("idjoueur",anchor=CENTER, width=80)
        table.column("pseudo",anchor=CENTER,width=80)
        table.heading("#0",text="",anchor=CENTER)
        table.heading("idjoueur",text="idjoueur",anchor=CENTER)
        table.heading("pseudo",text="pseudo",anchor=CENTER)
        for i in range(len(self.__Joueurs)):
            table.insert(parent='',index='end',iid=i,text='',values=(self.__Joueurs[i]))
        
    def Affiche_Parties(self):
        data = JoueurDB('pendu.db')
        self.__Parties = data.getParties()
        del data
            
        self._newWindow3 = Toplevel(self)
        self._newWindow3.title("Liste Parties")
        self._newWindow3.geometry("400x250")        
        table = ttk.Treeview(self._newWindow3)
        table.pack()
        table['columns'] = ('idpartie', 'idjoueur', 'mot', 'score')
        table.column("#0", width=0,  stretch=NO)
        table.column("idpartie",anchor=CENTER, width=80)
        table.column("idjoueur",anchor=CENTER,width=80)
        table.column("mot",anchor=CENTER,width=80)
        table.column("score",anchor=CENTER,width=80)
        table.heading("#0",text="",anchor=CENTER)
        table.heading("idpartie",text="idpartie",anchor=CENTER)
        table.heading("idjoueur",text="idjoueur",anchor=CENTER)
        table.heading("mot",text="mot",anchor=CENTER)
        table.heading("score",text="score",anchor=CENTER)
        for i in range(len(self.__Parties)):
            table.insert(parent='',index='end',iid=i,text='',values=(self.__Parties[i]))
            
class MonBoutonLettre(Button):
    def __init__(self, parent, fenet, indice,largeur):
        Button.__init__(self, master=parent, height= 2, width = largeur, text = chr(ord('A')+indice), state=DISABLED)
        
        self.__indice = indice
        self.__fenet = fenet
        self.__lettre = chr(ord('A')+self.__indice)
        self.config(command = self.cliquer)
    
    def cliquer(self):
        self.config(state = DISABLED)
        self.__fenet.traitement(self.__lettre)
    
    def getLettre(self):
        return self.__lettre

        
class ZoneAffichage(Canvas):
    def __init__(self, parent, largeur, hauteur, c):
        Canvas.__init__(self, parent, width=largeur, height=hauteur, bg = c)
        self.__listeFormes=[]
        # Base, Poteau, Traverse, Corde
        self.__listeFormes.append(Rectangle(self, 50,  270, 200,  26, "brown"))
        self.__listeFormes.append(Rectangle(self, 87,   83,  26, 200, "brown"))
        self.__listeFormes.append(Rectangle(self, 87,   70, 150,  26, "brown"))
        self.__listeFormes.append(Rectangle(self, 183,  67,  10,  40, "brown"))
        # Tete, Tronc
        self.__listeFormes.append(Rectangle(self, 178, 120,  20,  20, "black"))
        self.__listeFormes.append(Rectangle(self, 175, 143,  26,  60, "black"))
        # Bras gauche et droit
        self.__listeFormes.append(Rectangle(self, 133, 150,  40,  10, "black"))
        self.__listeFormes.append(Rectangle(self, 203, 150,  40,  10, "black"))
        # Jambes gauche et droite
        self.__listeFormes.append(Rectangle(self, 175, 205,  10,  40, "black"))
        self.__listeFormes.append(Rectangle(self, 191, 205,  10,  40, "black"))
    
    def setStateAllFormes(self, s):
        for i in self.__listeFormes:
             i.setState(s)
    def showForme(self,i):
        self.__listeFormes[i].setState('normal')
    def hideForme(self,i):
        self.__listeFormes[i].setState('hidden')
    def change_couleur_personnage(self,color):
        for i in range(len(self.__listeFormes)):
            if i > 3:
                self.__listeFormes[i].setCouleur(color)
    def change_couleur_potence(self,color):
        for i in range(len(self.__listeFormes)):
            if i < 4:
                self.__listeFormes[i].setCouleur(color)
    
if __name__ == '__main__':
    app = FenPrincipale()
    app.mainloop()     
            