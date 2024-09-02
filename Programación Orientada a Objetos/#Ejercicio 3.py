#Ejercicio 3
class Fraccion():
    def __init__(self, fraccion1, fraccion2):
       self.fraccion1 = fraccion1
       self.fraccion2 = fraccion2
    
    def __str__(self):
        return f"La primera fraccion es: {self.fraccion1}"
    
    def __add__(self, fraccion1, fraccion2 ):
        return Fraccion(
            self.fraccion1 + self.fraccion2 
        )
    def __mul__(self):
        return Fraccion(
            self.fraccion1 * self.fraccion2
        )
    
    def __eq__(self, fraccion1, fraccion2):
        return {fraccion1} == {fraccion2}

fraccion1 = Fraccion({3/5})
Fraccion2 = Fraccion({8/5})

print(fraccion1)