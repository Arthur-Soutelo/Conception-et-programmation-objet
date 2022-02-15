class Formes:
    def __init__(self,x,y):
        self.__pos = x,y
    
    def get_pos(self):
        return self.__pos
    
    def set_pos(self,newx,newy):
        self.__pos = newx,newy    
    
    def translation(self, dx,dy):
        posx,posy = self.__pos
        self.set_pos(posx+dx, posy+dy)
        pass
    
class Rectangle(Formes):
    def __init__(self, x, y, l, h):
        Formes.__init__(self, x, y)
        self.__dimensions = l,h
    
    def __str__(self):
        return "Rectangle : \n Dimensions : " + str(self.__dimensions) + "\n Origine : " + str(self.get_pos())

    def get_dim(self):
        return self.__dimensions
    
    def set_dim(self, newl, newh):
        self.__dimensions = newl,newh
        
    def contient_point(self, x,y):
       posx,posy = self.get_pos()
       l,h = self.get_dim()
       if (x >= posx and x < (posx+l)) and (y >= posy and y < (posy+h)):
           return True
       else:
           return False
      
    def redimension_par_points (self, x0,y0,x1,y1):
        self.__dimensions = abs(x1-x0),abs(y1-y0)
        if x0 < x1 and y0 < y1:
            self.set_pos(x0, y0)
        elif x0 > x1 and y0 < y1:
            self.set_pos(x1, y0)
        elif x0 < x1 and y0 > y1:
            self.set_pos(x0, y1)
        else:
            self.set_pos(x1, y1)
    

class Ellipse(Formes):
    def __init__(self, x, y, rx, ry):
        self.__rayon = rx,ry
        Formes.__init__(self, x, y)
        
    def __str__(self):
        return "Ellipse : \n Rayon(x,y): " + str(self.getr()) + "\n Origine : " + str(self.get_pos())
    
    def getr(self):
        return self.__rayon
    
    def setrxy(self, newrx, newry):
        self.__rayon = newrx,newry
    
    def contient_point(self, x,y):
       posx,posy = self.get_pos()
       rx,ry = self.getr()
       ray = ( (x-posx)**2 / (rx**2)  ) + ( (y-posy)**2 / (ry**2)  )
       if ray <= 1:
           return True
       else:
           return False
    
    def redimension_par_points (self, x0,y0,x1,y1):
        self.__rayon = abs(x1-x0),abs(y1-y0)
        self.set_pos(min(x0,x1)+(abs(x0+x1)/2), min(y0,y1)+(abs(y0+y1)/2))
        
class Cercle(Ellipse):
    def __init__(self, x, y, r):
        Ellipse.__init__(self, x, y, r, r)
        
    def __str__(self):
        return "Cercle : \n Rayon: " + str(self.getr()) + "\n Origine : " + str(self.get_pos())
        
    def getr(self):
        return self.getr()
    
    def setr(self, newr):
        self.setrxy = newr,newr
        
    def redimension_par_points (self, x0,y0,x1,y1):
        r = min(abs(x1-x0),abs(y1-y0))/2
        self.setr = r
        self.set_pos(min(x0,x1)+r, min(y0,y1)+r)
    