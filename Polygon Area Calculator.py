#When a Rectangle object is created, it should be initialized with width and height attributes. 

class shape_calculator:
    def __init__ (self, Rectangle, Square):
        self.rec = Rectangle
        self.sq = Square
    
    class Rectangle:
        def __init__(self, width, height):
            if width != str:
                self.width = width
                self.height = height
            else:
                self.width = int((width.split("="))[1])
                self.height = int((height.split("="))[1])
        
        def set_height(self, nheight):
            self.height = nheight

        def set_width(self, nwidth):
            self.width = nwidth

        def get_area(self):
            return (self.width * self.height)

        def get_perimeter(self):
            return (2 * self.width + 2 * self.height)

        def get_diagonal(self):
            return ((self.width ** 2 + self.height ** 2) ** .5)

        def __str__(self):      
            return ("Rectangle(width="+ str(self.width) +", height=" + str(self.height) + ")")

        def get_picture(self):
            if self.height > 50 or self.width > 50:
                return ('Too big for picture.')
            else:
                return ("*"*self.width + '\n') * self.height

        def get_amount_inside(self, kind):
            return (self.height * self.width) // (kind.height * kind.width)


    class Square(Rectangle):
        def __init__(self,width):
            self.width = width
            self.height = width

        def __str__(self):           
            return ("Square(side="+ str(self.width) + ")")

        def set_side(self, nwidth):
            self.height = nwidth
            self.width = nwidth

        def set_height(self, nwidth):
            self.height = nwidth
            self.width = nwidth

        def set_width(self, nwidth):
            self.width = nwidth
            self.height = nwidth
        


