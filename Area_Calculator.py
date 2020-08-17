class Rectangle:
    def __init__(self, width,height):
        self.height =  height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return ((2*self.width) + (2*self.height))

    def get_diagonal(self):
        return ((self.width**2) + (self.height**2))**0.5

    def get_picture(self):
        salida = ""
        if (self.width > 50 or self.height > 50): salida = "Too big for picture."
        else:
            for i in range(0,self.height):
                salida += "*"*self.width
                salida += "\n"
        return salida

    def get_amount_inside(self, otra_figura):
        fit_horizontal = 0
        fit_vertical = 0
        if (self.width >= otra_figura.width):
            fit_horizontal = self.width // otra_figura.width
        if (self.height >= otra_figura.height):
            fit_vertical = self.height // otra_figura.height
        salida = fit_horizontal*fit_vertical
        return salida 
    
    def __repr__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
    

class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side
        
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def __repr__(self):
        return "Square(side="+str(self.width)+")"
    def __str__(self):
        return "Square(side="+str(self.width)+")"
    

    

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
 
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
