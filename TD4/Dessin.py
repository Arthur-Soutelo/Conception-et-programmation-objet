from tkinter import *
from formes import *
from tkinter import colorchooser


class FenPrincipale(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(bg="grey")
        
        # paramètres de la fenêtre
        self.title('Application de dessin')
        self.geometry('500x500+400+400')
        
        # Frames
        Frame1 = Frame(self, borderwidth=2)
        Frame1.pack(side=TOP, padx=30, pady=30)
        
        Frame2 = Frame(self, borderwidth=2)
        Frame2.pack(side=BOTTOM, padx=30, pady=30)
        
        # constitution de l'arbre de scène
        boutonRectangle = Button(Frame1, text='Rectangle')
        boutonEllipse = Button(Frame1, text='Ellipse')
        boutonCouleur = Button(Frame1,text='Couleur')
        boutonQuitter = Button(Frame1,text='Quitter')
        
        self.canvas = ZoneAffichage(Frame2,500,500)
        
        boutonRectangle.config(command=self.canvas.selection_rectangle)
        boutonEllipse.config(command=self.canvas.selection_ellipse)
        boutonCouleur.config(command=self.canvas.selection_couleur)
        boutonQuitter.config(command=self.quit)  # idem
        
        boutonQuitter.config(bg='red')
        
        boutonRectangle.pack(side=LEFT, padx=10, pady=5)
        boutonEllipse.pack(side=LEFT, padx=10, pady=5)
        boutonCouleur.pack(side=LEFT, padx=10, pady=5)
        boutonQuitter.pack(side=LEFT, padx=10, pady=5)
        
        self.canvas.pack(side=BOTTOM, padx=5, pady=5)
        
        self.canvas.bind("<ButtonRelease-1>",self.release_canvas)
        self.canvas.bind("<Control-ButtonRelease-1>",self.effacer)
        
        
    def release_canvas(self,event):
        self.canvas.ajout_forme(event.x,event.y)
        
    def effacer(self,event):
        self.canvas.effacer_forme(event.x,event.y)
    

class ZoneAffichage(Canvas):
    def __init__(self, parent, largeur, hauteur):
        Canvas.__init__(self, parent, width=largeur, height=hauteur)
        self.type = 'Rectangle'
        self.couleur = 'red'
        self.formes = []
    
    def selection_rectangle(self):
        self.type = 'Rectangle'
        
    def selection_ellipse(self):
        self.type = 'Ellipse'
        
    def selection_couleur(self):
        colour = colorchooser.askcolor()
        self.couleur = colour[1]
        
    def ajout_forme(self,x,y):
        if self.type == 'Rectangle':
            x= Rectangle(self,x-10,y-10,20,20,self.couleur)
            self.formes.append(x)
        elif self.type == 'Ellipse':
           x = Ellipse(self, x, y, 20, 20, self.couleur)
           self.formes.append(x)
        #txt = self.create_text(200, 200, text="x='{}' , y='{}'".format(x, y), font="Arial 16 italic", fill="red")
         
    def effacer_forme(self,x,y):
        for forme in self.formes:
            if forme.contient_point(x, y) == 1:
                forme.effacer()
            
         
    

if __name__ == '__main__':
    app = FenPrincipale()
    app.mainloop()
